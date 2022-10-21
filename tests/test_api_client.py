import os
import sys
import pytest
import configparser

directory = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 
# setting path
sys.path.append(directory)

from jpo_patentapi_client import api_client
from jpo_patentapi_client import api_client_error

@pytest.fixture(scope="session")
def user_password():
  config = configparser.ConfigParser()
  config.read(os.path.dirname(os.path.abspath(__file__)) + '/config.ini')

  return {'user': config['api_test']['user'], 'password': config['api_test']['password']}

class TestJpoPatentapiClient:
  @pytest.mark.skip(reason='checked')
  def test_auth(self, user_password):
    client = api_client.ApiClient(user_password['user'], user_password['password'], 'https://ip-data.jpo.go.jp/auth/token')
    
    assert (client.tokens['access_token'] != "") & (client.tokens['refresh_token'] != "")
  
  @pytest.mark.skip(reason='checked')
  def test_unauth_illegal_username(self, user_password):
    with pytest.raises(api_client_error.ApiClientError):
      client = api_client.ApiClient('uso_user', user_password['password'], 'https://ip-data.jpo.go.jp/auth/token')
  
  @pytest.mark.skip(reason='checked')
  def test_unauth_illegal_password(self, user_password):
    with pytest.raises(api_client_error.ApiClientError):
      client = api_client.ApiClient(user_password['user'], 'usopass', 'https://ip-data.jpo.go.jp/auth/token')
  
  # @pytest.mark.skip(reason='checked')
  def test_get_token_by_refresh_token(self, user_password):
    client = api_client.ApiClient(user_password['user'], user_password['password'], 'https://ip-data.jpo.go.jp/auth/token')
    oldtokens = client.tokens
    client.get_token_by_refresh_token('https://ip-data.jpo.go.jp/auth/token')

    assert (client.tokens['access_token'] != "") & (client.tokens['refresh_token'] != "") & (client.tokens['access_token'] != oldtokens['access_token']) & (client.tokens['refresh_token'] != oldtokens['refresh_token'])



