import factory
from students.models import Student
from datetime import date


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student

    first_name = 'Test'
    last_name = 'User'
    email = factory.Sequence(lambda n: f'user{n}@test.com')
    enrollment_date = date.today()
    is_active = True
