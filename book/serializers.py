
from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
class categoryserailizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class Rentserializers(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = '__all__'
        
     
        
class Registerserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name','last_name')
    
        extra_kwargs = {
        'password' : {  'write_only' : True},
        }
        
        def create(self,validated_data):
            user = User.objects.create(username = validated_data['username'],password =  validated_data['password'],first_name = validated_data ['first_name'],last_name = validated_data ['last_name'])
            return user
        
        

class Transactionserializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        
        def create(self,validated_data):
            book_issue = Transaction.objects.create(book_name = validated_data ['book_name'],person_name =validated_data['person_name'],isuued_date = validated_data ['isuued_date'],rent_daily = validated_data ['rent_daily'])
            return book_issue        
        
        
class isuuedserializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['isuued_date','book_name']
        
class Booknameserializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['book_name','person_name']
        

class rentserializer(serializers.ModelSerializer):
    class Meta:
        model = Return
        fields = ['book_name','rent']
        
class Returnserializer(serializers.ModelSerializer):
    class  Meta:
        model = Return
        fields = ['book_name','total','person_name']