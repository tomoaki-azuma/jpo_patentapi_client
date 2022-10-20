import os
import sys
import pytest
import configparser

directory = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 
# setting path
sys.path.append(directory)

from jpo_patentapi_client import api_client

@pytest.fixture
def user_password():
  config = configparser.ConfigParser()
  config.read(os.path.dirname(os.path.abspath(__file__)) + '/config.ini')

  return {'user': config['api_test']['user'], 'password': config['api_test']['password']}

class TestJpoPatentapiClient:
  def test_auth(self, user_password):
    client = api_client.ApiClient(user_password['user'], user_password['password'], 'https://ip-data.jpo.go.jp/auth/token')
    
    assert (client.tokens['access_token'] != "") & (client.tokens['refresh_token'] != "")

