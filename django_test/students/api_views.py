from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.timezone import now
from datetime import timedelta
from django.db.models import Avg, F
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    search_fields = ['first_name', 'last_name', 'email']
    ordering_fields = ['first_name', 'enrollment_date', 'active']

    @action(detail=False, methods=['get'])
    def statistics(self, request):
        today = now().date()
        last_month = today - timedelta(days=30)

        ativos = Student.objects.filter(active=True)
        inativos = Student.objects.filter(active=False)

        media_dias = ativos.annotate(
            dias=today - F('enrollment_date')
        ).aggregate(avg=Avg('dias'))['avg']

        return Response({
            'ativos': ativos.count(),
            'inativos': inativos.count(),
            'media_dias_desde_matricula': media_dias,
            'matriculados_ultimo_mes': Student.objects.filter(
                enrollment_date__gte=last_month
            ).count(),
        })
