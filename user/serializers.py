from rest_framework import serializers
from .models import User, Survey, CourseDay
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_email(self, value):
        """
        Check that the email is unique and properly formatted.
        """
        validate_email(value)
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def validate_username(self, value):
        """
        Check that the username is unique.
        """
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already in use.")
        return value

    def create(self, validated_data):
        """
        Method to create a new user instance.
        """
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        """
        Method to update an existing user instance.
        """
        password = validated_data.pop('password', None)
        for field, value in validated_data.items():
            setattr(instance, field, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


# Custom serializer for obtaining tokens
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        if not username or not password:
            raise serializers.ValidationError("Both username and password are required.")

        try:
            user = User.objects.get(username=username)  # Find user by username
        except User.DoesNotExist:
            raise serializers.ValidationError("User with this username does not exist.")

        # Use check_password to verify the password
        if not user.check_password(password):
            raise serializers.ValidationError("Incorrect password.")

        # Continue validation with the original serializer
        return super().validate(attrs)


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'


class CourseDaySerializer(serializers.ModelSerializer):
    survey = SurveySerializer(many=False, read_only=True)

    class Meta:
        model = CourseDay
        fields = '__all__'
