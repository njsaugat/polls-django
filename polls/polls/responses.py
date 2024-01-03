class CustomResponse:
    def __init__(self, status_code,message,status,data=None):
        self.status_code=status_code
        self.status=status
        self.data=data
        self.message=message
        
    def get_response(self):
        response_dict={
            'statusCode':self.status_code,
            'status':self.status,
            'message':self.message,
            'data':self.data,
        }
        return response_dict
