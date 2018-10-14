from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class SystemUser(models.Model):
    rut = models.IntegerField(unique=True, default=0)
    check_digit = models.IntegerField(default=0)
    password = models.CharField(max_length=20,
                                default=User.objects.make_random_password())
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Admin(SystemUser):
    """
    An admin is a system user with full access to the system.
    """
    def __str__(self):
        return "%s, %s (%s)" % (self.last_name, self.first_name, "admin")


class NaturalPerson(SystemUser):
    """
    a Natural Person is a system user with limited permissions.
    """
    def __str__(self):
        return "%s, %s (%s)" % (self.last_name, self.first_name, "User")


class Course(models.Model):
    code = models.IntegerField()
    name = models.CharField(max_length=40)
    section_number = models.IntegerField(default=1)
    year = models.IntegerField(default=datetime.now().year)
    semester = models.CharField(max_length=15)

    def __str__(self):
        return "%s-%s %s" % (self.code, self.section_number, self.name)


class Coevaluation(models.Model):
    """
    for a co evaluation, the state field (open, close) is calculated from
    the end_date.
    """
    coev_identifier = models.CharField(max_length=40, default="Co-evaluation", blank=True)
    init_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(default=datetime.max)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    @property
    def open(self):
        return self.init_date < datetime.now() < self.end_date

    def __str__(self):
        return "%s (%s)" % (self.coev_identifier, self.course)


