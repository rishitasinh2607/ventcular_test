from rest_framework import serializers
from app1.models import Users

class UserSerializer(serializers.ModelSerializer):
    customer_id = serializers.CharField(required=False)  #all this are provided to just edit any particular field not to madate edit all the fields 
    name = serializers.CharField(required=False)
    

    class Meta:
        model = Users
        fields = '__all__' 