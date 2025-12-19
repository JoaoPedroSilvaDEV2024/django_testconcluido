from rest_framework import serializers
from datetime import date
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_email(self, value):
        if not value.endswith(('.edu', '.edu.br')):
            raise serializers.ValidationError(
                'Email deve ser educacional (.edu ou .edu.br)'
            )
        return value

    def validate_enrollment_date(self, value):
        if value > date.today():
            raise serializers.ValidationError(
                'Data de matrícula não pode ser futura'
            )
        return value

    def validate(self, data):
        nome_completo = data['first_name'] + data['last_name']
        if len(nome_completo) < 5:
            raise serializers.ValidationError(
                'Nome completo deve ter no mínimo 5 caracteres'
            )
        return data
