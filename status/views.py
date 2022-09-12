from rest_framework import views,response, permissions

from user import authentication
from . import serializer as status_serializer
from . import services



class StatusCreateListApi(views.APIView):
    authentication_classes=(authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        serializer = status_serializer.StatusSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        # create a status
        serializer.instance = services.create_status(user=request.user, status=data)

        return response.Response(data=serializer.data)

    def get(self, request):
        status_collection = services.get_user_status(user=request.user)
        serializer = status_serializer.StatusSerializer(status_collection,many=True) 
        # many true we tell django that will be zero or more objcects
        return response.Response(data=serializer.data)

class StatusRetrieveUpdateDelete(views.APIView):
    authentication_classes=(authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, status_id):
        status = services.get_user_status_detail(user=request.user, status_id=status_id)
        serializer = status_serializer.StatusSerializer(status) # we dont need many=True
        return response.Response(data=serializer.data)
