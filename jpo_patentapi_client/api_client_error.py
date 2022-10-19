class ApiClientError(Exception):
  
  def __init__(self, message, http_status, api_status, access_count):
    error_message = """JPO API Access Error : http status code(%s), JPO API status code(%s)
    Error Meassage: %s
    Remain Access Count: %s
    """ % (http_status.to_s(), api_status.to_s(), access_count.to_s())
    
    super.__init__(error_message)

    