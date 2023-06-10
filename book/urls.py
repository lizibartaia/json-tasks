from django.urls import path
from .views import book_detail

app_name = 'book'

urlpatterns = [
    path('<int:book_id>/', book_detail, name='detail'),
]