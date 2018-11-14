from django.db import models

# Create your models here.


class Address(models.Model):
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64, null=True, blank=True)
    home_number = models.CharField(max_length=8, null=True, blank=True)
    flat_number = models.CharField(max_length=8, null=True, blank=True)

    def __str__(self):
        return "{} {} {} {}".format(self.city, self.street, self.home_number, self.flat_number)

class Person(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32, null=True, blank=True)
    note = models.TextField(null=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{} {} {}".format(self.name, self.surname, self.note)

class Phone(models.Model):

    TYPE_NUM_CHOICES = [
        (1, 'Mobile'),
        (2, 'Work'),
        (3, 'Home'),
        (4, 'Other')
    ]
    phone_number = models.CharField(max_length=13, unique=True)
    type_number = models.IntegerField(choices=TYPE_NUM_CHOICES)
    persons = models.ForeignKey(Person, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{} {}".format(self.phone_number, self.type_number)


class Email(models.Model):

    TYPE_EMAIL_CHOICES = [
        (1, 'Home'),
        (2, 'Work'),
        (3, 'Other')
    ]

    email_address = models.EmailField(max_length=64, unique=True)
    type_email = models.IntegerField(choices=TYPE_EMAIL_CHOICES)
    persons = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return "{} {}".format(self.email_address, self.type_email)


class Group(models.Model):
    title = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True)
    persons = models.ManyToManyField(Person, related_name='group', blank=True)

    def __str__(self):
        return "{} {}".format(self.title, self.description)
