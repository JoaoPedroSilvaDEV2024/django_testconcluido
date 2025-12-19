from django.db import models
from django.db.models import Count, Prefetch
from django.utils import timezone


# =========================
# MANAGERS
# =========================

class StudentQuerySet(models.QuerySet):
    def with_course_count(self):
        return self.annotate(course_count=Count('enrollments'))

    def active_with_courses(self):
        return (
            self.filter(is_active=True)
            .prefetch_related(
                Prefetch(
                    'enrollments',
                    queryset=Enrollment.objects.select_related('course')
                )
            )
        )


class StudentManager(models.Manager):
    def get_queryset(self):
        return StudentQuerySet(self.model, using=self._db)

    def with_course_count(self):
        return self.get_queryset().with_course_count()

    def active_with_courses(self):
        return self.get_queryset().active_with_courses()


class CourseManager(models.Manager):
    def popular(self):
        return self.annotate(
            student_count=Count('enrollments')
        ).filter(student_count__gt=5)


# =========================
# MODELS
# =========================

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField()
    is_active = models.BooleanField(default=True)

    objects = StudentManager()

    class Meta:
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Course(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=20, unique=True)
    credits = models.IntegerField()
    description = models.TextField()

    objects = CourseManager()

    class Meta:
        indexes = [
            models.Index(fields=['code']),
        ]

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('enrolled', 'Enrolled'),
        ('completed', 'Completed'),
        ('dropped', 'Dropped'),
    ]

    student = models.ForeignKey(
        Student,
        related_name='enrollments',
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course,
        related_name='enrollments',
        on_delete=models.CASCADE
    )
    enrolled_date = models.DateField(default=timezone.now)
    grade = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )

    class Meta:
        indexes = [
            models.Index(fields=['student', 'course']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return f'{self.student} - {self.course}'
from django.db import models
from django.db.models import Count, Prefetch
from django.utils import timezone


# =========================
# MANAGERS
# =========================

class StudentQuerySet(models.QuerySet):
    def with_course_count(self):
        return self.annotate(course_count=Count('enrollments'))

    def active_with_courses(self):
        return (
            self.filter(is_active=True)
            .prefetch_related(
                Prefetch(
                    'enrollments',
                    queryset=Enrollment.objects.select_related('course')
                )
            )
        )


class StudentManager(models.Manager):
    def get_queryset(self):
        return StudentQuerySet(self.model, using=self._db)

    def with_course_count(self):
        return self.get_queryset().with_course_count()

    def active_with_courses(self):
        return self.get_queryset().active_with_courses()


class CourseManager(models.Manager):
    def popular(self):
        return self.annotate(
            student_count=Count('enrollments')
        ).filter(student_count__gt=5)


# =========================
# MODELS
# =========================

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField()
    is_active = models.BooleanField(default=True)

    objects = StudentManager()

    class Meta:
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['is_active']),
        ]

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Course(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=20, unique=True)
    credits = models.IntegerField()
    description = models.TextField()

    objects = CourseManager()

    class Meta:
        indexes = [
            models.Index(fields=['code']),
        ]

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('enrolled', 'Enrolled'),
        ('completed', 'Completed'),
        ('dropped', 'Dropped'),
    ]

    student = models.ForeignKey(
        Student,
        related_name='enrollments',
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        Course,
        related_name='enrollments',
        on_delete=models.CASCADE
    )
    enrolled_date = models.DateField(default=timezone.now)
    grade = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )

    class Meta:
        indexes = [
            models.Index(fields=['student', 'course']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return f'{self.student} - {self.course}'
