from rest_framework import serializers

from user import serializer as user_serializer

from . import services

class StatusSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    content = serializers.CharField()
    date_published= serializers.DateTimeField()

    # user - we can take him on two ways
    # user_id = serializers.IntegerField()

    # we take user as JSON representation
    user = user_serializer.UserSerializer(read_only=True) 

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        return services.StatusDataClass(**data)

