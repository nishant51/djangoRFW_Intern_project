from .models import Task
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id', 
            'title', 
            'body', 
            'status',
        )

#validationerror for the respective fields if any of them are left without data
    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Title cannot be empty")
        return value

    def validate_body(self, value):
        if not value:
            raise serializers.ValidationError("Body cannot be empty")
        return value

    def validate_status(self, value):
        if not value:
            raise serializers.ValidationError("Status cannot be empty")
        return value
