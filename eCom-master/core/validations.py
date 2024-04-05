from django.core.exceptions import ValidationError
import re




def validate_name(value):
    pattern =  r'^[a-zA-Z ]{2,20}$'
    if not re.match(pattern, value):
        raise ValidationError(u'%s violates constraints. Please verify and enter again' % value)
    
def validate_email(value):
    pattern = r'^[\w\.]{3,30}@[\w\.]+\.\w+$'
    if not re.match(pattern, value):
        raise ValidationError(u'%s violates constraints. Please verify and enter again' % value)
    
def validate_username(value):
    pattern = r'^[\w\.]{3,30}$'
    if not re.match(pattern, value):
        raise ValidationError(u'%s violates constraints. Please verify and enter again' % value)
    
def validate_description(value):
    pattern = r'^[a-zA-Z \.\,\-\s]{3,50}$'
    if not re.match(pattern, value):
        raise ValidationError(u'%s violates constraints. Please verify and enter again' % value)