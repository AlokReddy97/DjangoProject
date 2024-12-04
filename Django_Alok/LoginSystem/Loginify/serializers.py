from rest_framework import serializers
from Loginify.models import UserDetails

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['username', 'email', 'password']

    def validate_email(self, value):
        """
        Check if the email already exists for another user when updating.
        """
        if UserDetails.objects.filter(email=value).exists() and self.instance.email != value:
            raise serializers.ValidationError("Email already in use by another user.")
        return value
