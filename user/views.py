from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
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


class SurveyComparisonView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, user_id):
        surveys = Survey.objects.filter(userid=user_id).order_by('-id')[:2]

        if not surveys:
            return Response({"error": "No survey data found"}, status=404)

        data = {}

        # Обработка текущего опроса
        survey_current = surveys[0]
        data["current"] = {
            "hours": survey_current.hours,
            "enoughSleep": survey_current.enoughSleep,
            "tiredness": survey_current.tiredness,
            "quality": survey_current.quality,
            "fallingAsleep": survey_current.fallingAspleep,
            "nightWaking": survey_current.nightWaking,
            "electronicDevices": survey_current.electronicDevices,
            "routine": survey_current.routine,
            "caffeine": survey_current.caffeine,
            "refreshed": survey_current.refreshed,
        }

        # Обработка предыдущего опроса, если он существует
        if len(surveys) > 1:
            survey_previous = surveys[1]
            data["previous"] = {
                "hours": survey_previous.hours,
                "enoughSleep": survey_previous.enoughSleep,
                "tiredness": survey_previous.tiredness,
                "quality": survey_previous.quality,
                "fallingAsleep": survey_previous.fallingAspleep,
                "nightWaking": survey_previous.nightWaking,
                "electronicDevices": survey_previous.electronicDevices,
                "routine": survey_previous.routine,
                "caffeine": survey_previous.caffeine,
                "refreshed": survey_previous.refreshed,
            }

        return Response(data)
