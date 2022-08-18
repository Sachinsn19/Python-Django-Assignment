from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Products
from django.utils import timezone 
from datetime import timedelta

class UserSerializer(serializers.ModelSerializer):
    products = serializers.SlugRelatedField(many=True, slug_field='name', queryset = Products.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username','email','products']

MIN_LENGTH = 8
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=MIN_LENGTH, write_only=True, 
                error_messages={"min_length":f"Passwords must be longer than {MIN_LENGTH} characters"})
    password2 = serializers.CharField(min_length=MIN_LENGTH, write_only=True, 
                error_messages={"min_length":f"Passwords must be longer than {MIN_LENGTH} characters"})
    class Meta:
        model=User
        fields = ('username', 'first_name','last_name','email','password','password2')
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Passwords doesn't match")
        return super().validate(attrs)
    def create(self, validated_data):
        user = User.objects.create(
                username = validated_data['username'],
                email = validated_data['email'],
                first_name = validated_data['first_name'],
                last_name = validated_data['last_name'],
                )
        
        user.set_password(validated_data['password'])
        user.save()
        return user

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Products
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id',instance.id)
        instance.owner = validated_data.get('owner',instance.owner)
        instance.name = validated_data.get('name',instance.name)
        instance.category = validated_data.get('category',instance.category)
        instance.cost = validated_data.get('cost',instance.cost)
        instance.discount = validated_data.get('discount',instance.discount)
        instance.created = validated_data.get('created',instance.created)
        instance.is_active = True
        if (timezone.now() > instance.created + timedelta(days=60)):
            instance.is_active = validated_data.get('is_active',instance.is_active)
        instance.save()
        return instance

