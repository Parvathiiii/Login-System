from rest_framework import serializers
from accounts.models import LoginDetails

class LoginDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LoginDetails
        fields = ['Username','Password','Email','FirstName','LastName']
