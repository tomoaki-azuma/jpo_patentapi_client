import requests
import json
from . import api_client_error

class ApiClient:
  HOST = "ip-data.jpo.go.jp"
  HEADER = {"Content-Type": "application/x-www-form-urlencoded", "Host": "ip-data.jpo.go.jp"}

  def __init__(self, user, password, url):
    self.tokens = self.__get_token(user, password, url)
  
  def __get_token(self, user ,password, url):
    payload = {'grant_type': 'password', 'username': user, 'password': password}
    r = requests.post(url, headers=self.HEADER, data=payload)
    tokens  = {"access_token": "", "refresh_token": ""}
    if (r.status_code == 200):
      tokens["access_token"] = r.json()['access_token']
      tokens["refresh_token"] = r.json()['refresh_token']
      return tokens
    elif (r.status_code in ['401', '429', '500', '504']):
      raise api_client_error.ApiClientError(r.result.message, r.status_code, r.result.statusCode, r.result.remainAccessCount)
    else:
      message = 'HTTP 400 Bad Request'
      raise api_client_error.ApiClientError(message, r.status_code, '', '')
  
  def get_token_by_refresh_token(self, url):
    print('get_token_by_refresh')
    print(self.tokens)
    payload = {'grant_type': 'refresh_token ', 'refresh_token': self.tokens['refresh_token']}
    r = requests.post(url, headers=self.HEADER, data=payload)
    new_tokens  = {"access_token": "", "refresh_token": ""}
    if (r.status_code == 200):
      new_tokens["access_token"] = r.json()['access_token']
      new_tokens["refresh_token"] = r.json()['refresh_token']
      self.tokens = new_tokens
      print(self.tokens)
      return
    elif (r.status_code in ['401', '429', '500', '504']):
      raise api_client_error.ApiClientError(r.result.message, r.status_code, r.result.statusCode, r.result.remainAccessCount)
    else:
      message = 'HTTP 400 Bad Request'
      raise api_client_error.ApiClientError(message, r.status_code, '', '')