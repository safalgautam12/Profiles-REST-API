from rest_framework.views import APIView
from rest_framework.response import Response #Response is used to return response when api view is called 



class HelloApiView(APIView):
    """Test API View"""
    
    #request is passed by django
    def get(self, request, fromat=None):
        """Returns a list of APIView features"""
        an_apiview=[
            'Uses HTTP methods as function (get, post, patch , put , delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ] 
        return Response({'message':'Hello!', 'an_apiview':an_apiview})