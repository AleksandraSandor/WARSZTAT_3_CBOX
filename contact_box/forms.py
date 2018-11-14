from django.forms import ModelForm
from .models import Address, Person, Phone, Email, Group
from django import forms



class PostForm(ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'surname', 'note')

class FormsForm(ModelForm):
    class Meta:
        model = Address
        fields = ('city', 'street', 'home_number', 'flat_number')


class PhoneForm(ModelForm):
    class Meta:
        model = Phone
        fields = ('phone_number', 'type_number')

class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ('email_address', 'type_email')

class AddressForm(ModelForm):
    class Meta:
        model = Person
        fields = ('address', )

class GroupForm(ModelForm):
    class Meta:
        model = Group
        exclude = ["people"]
        fields = ('title', 'description', 'persons')
