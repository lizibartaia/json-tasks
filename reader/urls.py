from django.urls import path
from .views import enter_personal_data

app_name = 'reader'

urlpatterns = [
    path('enter/', enter_personal_data, name='enter'),
]