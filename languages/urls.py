from django.urls import path, include
from rest_framework import routers
from .views import LanguageView, ProgrammerView, ParadigmView

router = routers.DefaultRouter()
router.register('languages',   LanguageView)
router.register('programmers', ProgrammerView)
router.register('paradigms',   ParadigmView)

urlpatterns = [
	path("", include(router.urls))
]
