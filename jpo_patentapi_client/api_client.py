import requests
import json
# import api_client_error

class ApiClient:
  HOST = "ip-data.jpo.go.jp"
  HEADER = {"Content-Type": "application/x-www-form-urlencoded", "Host": "ip-data.jpo.go.jp"}

  def __init__(self, user, password, url):
    self.__get_token(user, password, url)
  
  def __get_token(self, user ,password, url):
    payload = {'grant_type': 'password', 'username': user, 'password': password}
    r = requests.post(url, headers=self.HEADER, data=payload)
    print(r.status_code)
    tokens  = {"access_token": "", "refresh_token": ""}
    if (r.status_code == 200):
      tokens["access_token"] = r.json()['access_token']
      tokens["refresh_token"] = r.json()['refresh_token']
      return tokens
    elif (r.status_code in ['401', '429', '500', '504']):
      print(r)
    else:
      print(r)
      pass
    