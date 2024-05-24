from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from user.views import UserViewSet, MyTokenObtainPairView, CourseDayViewSet, SurveyViewSet, CourseViewSet, \
    SurveyComparisonView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'course-days', CourseDayViewSet)
router.register(r'surveys', SurveyViewSet)
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/auth/', include('dj_rest_auth.urls')),
    path('api/v1/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/token/', include('djoser.urls.authtoken')),
    path('api/v1/auth/password/reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/v1/survey-comparison/<int:user_id>/', SurveyComparisonView.as_view(), name='survey-comparison'),

]
