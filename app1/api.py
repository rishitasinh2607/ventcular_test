from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import *

class UserAuthentication( Token):
    def post(self,request,*args,**kwargs):
        serializer = self.serializer_class(data=request.data,context={"request":request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token.created = Token.objects.get_orcreate(user=user)
        return Response(Token.key)

class UserList(APIView):
    def get(self,request):
        model = Users.objects.all()
        serializer = UserSerializer(model,many=True)
        return Response(serializer.data)
    def post(self,request):
        model = Users.objects.all()
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTTP_400_BAD_REQUEST)

class UserDetail(APIView): #diff url so create diff clASS for this 

    def get_user(self,customer_id):   #search criteria for data 
        try:
            model = Users.objects.get(id=customer_id)
            return model
        except Users.DoesNotExits:
            return 
    
    def get(self,request,customer_id): #methods
        if not self.get_user(customer_id):
           return  Response(f'user with(customer_id)is not found in db',status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(self.get_user(customer_id))
        return Response(serializer.data)
   
    def put(self,request,customer_id):   #to manipulate data
        serializer =  UserSerializer(self.get_user(customer_id),data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTTP_400_BAD_REQUEST)
    
    def delete(self,request,customer_id):
        if not self.get_user(customer_id):
               return  Response(f'user with(customer_id)is not found in db',status=status.HTTP_404_NOT_FOUND)
        model =  self.get_user(customer_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
   
    