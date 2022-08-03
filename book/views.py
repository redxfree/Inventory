from django.shortcuts import redirect, render
from .serializers import *
from .models import *
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.filters import SearchFilter
from django.urls import reverse_lazy
from django_filters.rest_framework import DjangoFilterBackend
from django.views.generic.base import TemplateView

# Create your views here.
class Api(TemplateView):

    template_name = 'templates/base.html'
    
    # def post(self,request):
    #     return render(self.request,self.template_name)
    


class RegisterAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Registerserializers
    template_name  = 'register.html'
    
    def post(self,request):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        
        return Response ({
            "message" : "Registered successfully" 
        })
    
    
class Bookname(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer
    filter_backends = [SearchFilter]
    search_fields = ['$name']
    template_name = 'name.html'
  
class Bookrent(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer
    filter_backends = [SearchFilter]
    search_fields = ['$name']
      
    
class Bookcategory(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
        
        
        
class Bookisuued(generics.CreateAPIView):
    queryset =Transaction.objects.all()
    serializer_class = Transactionserializer
    lookup_field = 'book_name'
    
    def post(self,request):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        
        return Response ({
            "message" : "Book Issued successfully" 
        })
    
    
    
class Bookreturn(generics.ListAPIView):
    queryset =Transaction.objects.all()
    serializer_class = Returnserializer
    lookup_field = ['book_name','rent']
    
    def post(self,request):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        
        return Response ({
            "message" : "Book returned successfully" 
        })
    
    
        
class Bookissuedlists(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = Booknameserializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['book_name']
  

class Totalrent(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = rentserializer
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['rent']
    
    
class Boookperson(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = Booknameserializer
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['person_name']


class Bookissuedlist(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = isuuedserializer
    filter_backends =[DjangoFilterBackend]
    filterset_fields = ['isuued_date']    