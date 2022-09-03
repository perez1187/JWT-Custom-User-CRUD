from rest_framework import serializers
from . import services


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) # because we dont whant anyone to change ID
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.CharField()
    password= serializers.CharField(write_only=True) # becasue we dont whant to show password

    # in services we created "views"  and now we can overwrite serialzier
    # however it is not that important? it is because there are some problem with other views, but
    # it is programmer dependent

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        return services.UserDataClass(**data) # **data -> unpacked data
