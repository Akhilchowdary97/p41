from rest_framework.views import APIView
#response will be given from response function
from rest_framework.response import Response
from myapp.serializers import HelloSerializer
class HelloApiView(APIView):
    serializer_class=HelloSerializer
    ''' The get method is responsible for handling the get responses'''
    def get(self,request,format=None):
        #always response should in the form of dictionary
        return Response({'name':"HelloAPIView",'message':"Hello Akhil",'request_type':'get'})
    def post(self,request,format=None):
        data=request.data.get('none')
        return Response({'message':"Hello Akhil,Welcome to post","request_type":"POST",'data':data})
    def put(self,request,format=None):
        data=request.data.get('none')
        return Response({'message':"Hello Akhil Welcome to put","request_method":"PUT",'data':data})
    def patch(self,request,format=None):
        data=request.data.get('none')
        return Response({'message':"Hello Akhil Welcome to patch","request_method":"PATCH",'data':data})
    def delete(self,request,format=None):
        data=request.data.get('none')
        return Response({'message':"Hello Akhil Welcome to delete","request_type":"DELETE",'data':data})
    