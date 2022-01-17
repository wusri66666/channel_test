from django.urls import path
from app.apis import *

urlpatterns = [
    path('people/', Test1APIView.as_view()),
    path('throw_error/', Test2APIView.as_view()),
]
