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
        pass
