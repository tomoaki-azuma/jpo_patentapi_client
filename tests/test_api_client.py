import os
import sys

directory = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 
# setting path
sys.path.append(directory)

from jpo_patentapi_client import api_client

class TestJpoPatentapiClient:
  def test_one(self):
    client = api_client.ApiClient('user', 'passwd', 'https://ip-data.jpo.go.jp')

    assert 1 == 2

