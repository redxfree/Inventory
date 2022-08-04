from django.urls import path
from .views import *


urlpatterns = [
        path('register/',RegisterAPI.as_view()),
   #   path('',Api.as_view()),
       path('name/',Bookname.as_view()),
       path('rent/',Bookrent.as_view()),
       path('cat/',Bookcategory.as_view()),
       path('issue/',Bookisuued.as_view()),
       path('return/',Bookreturn.as_view()),
       path('list/',Bookissuedlists.as_view()),
       path('total/',Totalrent.as_view()),
       path('person/',Boookperson.as_view()),
       path('is/',Bookissuedlist.as_view())
]