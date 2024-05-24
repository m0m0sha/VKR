from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User, CourseDay, Survey, Course
from .serializers import UserSerializer, MyTokenObtainPairSerializer, CourseDaySerializer, SurveySerializer, \
    CourseSerializer


class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = [AllowAny]


# Custom view for obtaining tokens
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CourseDayViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       viewsets.GenericViewSet):
    queryset = CourseDay.objects.all()
    serializer_class = CourseDaySerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = [AllowAny]


class SurveyViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = [AllowAny]


class CourseViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = [AllowAny]
