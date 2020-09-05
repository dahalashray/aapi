from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True, required=False)


    def create(self,validated_data):
        if User.objects.filter(username = validated_data.get('username')).exists():
            raise serializers.ValidationError("Username already taken.")

        if not validated_data.get('password') or not validated_data.get('confirm_password'):
            raise serializers.ValidationError("Please enter a password and "
                "confirm it.")

        if validated_data.get('password') != validated_data.get('confirm_password'):
            raise serializers.ValidationError("Those passwords don't match.")

        user = User.objects.create_user(username=validated_data.get('username'), password=validated_data.get('password'))
        return user
    

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance


    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'confirm_password',]
        read_only_fields = ['confirm_password',]