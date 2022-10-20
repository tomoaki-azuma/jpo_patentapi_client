import os
import sys

directory = os.path.abspath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 
# setting path
sys.path.append(directory)

from jpo_patentapi_client import api_client

class TestJpoPatentapiClient:
  def test_one(self):
    client = ApiClient('user', 'passwd', 'url')
    assert 1 == 1

