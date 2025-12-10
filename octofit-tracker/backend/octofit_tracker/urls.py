"""
octofit_tracker URL Configuration

REST API endpoints are available at:
    https://$CODESPACE_NAME-8000.app.github.dev/api/[component]/
    http://localhost:8000/api/[component]/
Replace $CODESPACE_NAME with your actual Codespace name.
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'activities', ActivityViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'leaderboard', LeaderboardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
