from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import * 
from schedule.models import * 
from django.contrib.auth.password_validation import validate_password

class LoginSer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
    

class userSer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class auditSer(serializers.ModelSerializer):
    class Meta:
        model = Auditory
        fields = "__all__"

class HistorySer(serializers.Serializer):
    user = userSer()
    auditory = auditSer()
    last_pick = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    status = serializers.IntegerField()