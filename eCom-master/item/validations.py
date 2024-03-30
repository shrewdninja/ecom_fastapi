from django.core.exceptions import ValidationError
import re
from datetime import datetime




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
    

def validate_date(value):
    if value[0:4].isdigit()==False or value[4]!='/' or value[5:7].isdigit()==False or len(value)!=7 or int(value[5:7])>12 or int(value[5:7])==0:
        raise ValidationError(u'%s violates constraints. Please verify and enter again' % value)
    else:
        if(int(value[0:4])<datetime.now().year):
            raise ValidationError("Card has expired. Please enter a different card.")
        elif(int(value[0:4])==datetime.now().year and int(value[5:7])<datetime.now().month):
            raise ValidationError("Card has expired. Please enter a different card.")

def validate_price(value):
    if float(value)<0 or float(value)>999999:
        raise ValidationError(u'%s violates constraints. Please verify and enter again' % value)