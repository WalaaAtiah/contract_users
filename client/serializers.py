from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        extra_kwargs = {
            'Name': {'required': True},
            'Contract_Start_Date': {'required': True},
            'Contract_End_Date': {'required': True},

		}
    def validate(self, data):
        if data['Contract_Start_Date'] > data['Contract_End_Date']:
            raise serializers.ValidationError({"Contract_Date": "The contract start date must be before the contract end date"})
        return data

    


