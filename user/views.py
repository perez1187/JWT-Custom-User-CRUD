
# we can call it for example apis:

from rest_framework import views, response, exceptions, permissions

from . import serializer as user_serializer
from . import services

class RegisterApi(views.APIView):

    # this only allow post request
    def post(self, request):
        serializer = user_serializer.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) # if not valid, we raise exception

        data= serializer.validated_data

        # in that moment we just print data
        print(data)

        serializer.instance = services.create_user(user_dc=data)

        return response.Response(data=serializer.data) # from testing we writed return response.Response(data={"hello": "World"}) 
