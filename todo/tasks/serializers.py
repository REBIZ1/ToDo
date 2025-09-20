from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('id', 'owner', 'created_at', 'updated_at')

    owner = serializers.ReadOnlyField(source='owner.username')