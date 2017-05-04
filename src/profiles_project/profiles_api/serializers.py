from rest_framework import serializers

from .models import UserProfile

#
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""

    # Just like Model
    # CharField, BooleanFields and others are pre-defined fields
    name = serializers.CharField(max_length=10)

    # serializers fields have pre-defined validation

# It's model serializer
class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects"""

    class Meta:
        # model which we point to
        model = UserProfile
        # take the field
        fields = ('id', 'email', 'name', 'password')
        # we don't want for user to see password
        # Define which specific field for keyword
        # Set the password write only
        extra_kwargs = {'password': {'write_only': True}}

    # Set password correctly!
    def create(self, validated_data):
        """Create and Return a new user."""
        user = UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
