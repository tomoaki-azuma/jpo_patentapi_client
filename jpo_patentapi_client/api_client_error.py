class ApiClientError(Exception):
  
  def __init__(self, message, http_status, api_status, access_count):
    error_message = """JPO API Access Error : http status code(%s), JPO API status code(%s)
    Error Meassage: %s
    Remain Access Count: %s
    """ % (str(http_status), str(api_status), message, str(access_count))
    
    return super().__init__(error_message)

    