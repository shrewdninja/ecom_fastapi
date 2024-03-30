from django.core.exceptions import ValidationError
import re




def validate_name(value):
    pattern =  r'^[a-zA-Z ]{2,20}$'
    if not re.match(pattern, value):
        raise ValidationError(u'%s violates constraints. Please verify and enter again' % value)
    
def validate_email(value):
    pattern = r'^[\w\.]+@[\w\.]+\.\w+$'
    if not re.match(pattern, value):
        raise ValidationError(u'%s violates constraints. Please verify and enter again' % value)
    
def validate_username(value):
    pattern = r'^[\w\.]$'
    if not re.match(pattern, value):
        raise ValidationError(u'%s violates constraints. Please verify and enter again' % value)
    
def validate_description(value):
    pattern = r'^(.|\s)+[\w\.]+(.|\s)$'
    if not re.match(pattern, value):
        raise ValidationError(u'%s violates constraints. Please verify and enter again' % value)
    
def validate_card(value):
    if value.isdigit()==False or len(value)!=16:
        raise ValidationError(u'%s violates constraints. Please verify and enter again' % value)
    

def validate_cvv(value):
    if value.isdigit()==False or len(value)!=3:
        raise ValidationError(u'%s violates constraints. Please verify and enter again' % value)

def validate_price(value):
    if float(value)<0 or float(value)>999999:
        raise ValidationError(u'%s violates constraints. Please verify and enter again' % value)