from rest_framework import serializers


#
class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""

    # Just like Model
    # CharField, BooleanFields and others are pre-defined fields
    name = serializers.CharField(max_length=10)

    # serializers fields have pre-defined validation
