from django import template
from contact_box.models import Phone, Email
register = template.Library()


@register.filter
def queryset_to_list(value):
    return ", ".join([str(x) for x in value]) if value else "None"

@register.filter(name='phone_type')
def phone_type(type_number):
    if type_number == 1:
        return 'Mobile'
    elif type_number == 2:
        return 'Work'
    elif type_number == 3:
        return 'Home'
    elif type_number == 4:
        return 'Other'
    else:
        return 'Indefinite'


@register.filter(name='email_type')
def email_type(type_email):
    if type_email == 1:
        return 'Home'
    elif type_email == 2:
        return 'Work'
    elif type_email == 3:
        return 'Other'
    else:
        return 'Indefinite'