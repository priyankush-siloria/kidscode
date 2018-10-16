from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^$', HomePage.as_view(), name="homepage"),
	url(r'^schedule$', SchedulePage.as_view(), name="schedule"),
	url(r'^daypreferences$', DayPreferences.as_view(), name="daypreferences"),
]
