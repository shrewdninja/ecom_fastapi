from django import forms
from .models import Item, Order
from .validations import validate_card, validate_description, validate_date, validate_email,validate_name, validate_username,validate_cvv, validate_price

INPUT_CLASSES = 'w-full px-6 py-4 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('category', 'name', 'description', 'price', 'image')
        name=forms.CharField(widget=forms.TextInput(attrs={
                'placeholder': 'Enter name',
                'class': 'w-full py-4 px-6 rounded-xl'
            }), validators=[validate_name])
        description=forms.CharField(
               widget=forms.TextInput(attrs={
               'placeholder': 'Enter details here',
               'class': 'w-full px-6 py-4 rounded-xl border'
          }), validators=[validate_description])
        price = forms.FloatField(
            min_value=0, max_value= 999999,
            widget=forms.NumberInput(
                attrs={'step': "0.01"}
                ), validators=[validate_price]
                ) 
        widgets={
            'category': forms.Select(attrs={
            'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
            'class': INPUT_CLASSES            
            }),
            'description': forms.Textarea(attrs={
            'class': INPUT_CLASSES
            }),
            'price': forms.NumberInput(attrs={
            'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
            'class': INPUT_CLASSES
            })
        }

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=('name', 'card_number', 'cvv','expiry_date', 'address')
        name=forms.CharField(widget=forms.TextInput(attrs={
                'placeholder': 'Enter name on the card',
                'class': 'w-full py-4 px-6 rounded-xl'
            }), validators=[validate_name])
        card_number=forms.CharField(
               widget=forms.TextInput(attrs={
               'placeholder': 'Enter card number',
               'class': 'w-full py-4 px-6 rounded-xl'
          }), validators=[validate_card])
        cvv=forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Enter CVV',
            'class': 'w-full py-4 px-6 rounded-xl'
        }), validators=[validate_cvv])
        expiry_date=forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Enter expiry date in YYYY/MM format only',
            'class': 'w-full py-4 px-6 rounded-xl'
        }), validators=[validate_date])
        
        address = forms.CharField(
               widget=forms.TextInput(attrs={
               'placeholder': 'Enter your address',
               'class': 'w-full px-6 py-4 rounded-xl border'
          }), validators=[validate_description])
                 
        widgets={
            'name': forms.TextInput(attrs={
            'class': INPUT_CLASSES            
            }),
            'card_number': forms.TextInput(attrs={
            'class': INPUT_CLASSES       
            }),
            'cvv': forms.TextInput(attrs={
            'class': INPUT_CLASSES            
            }),
            'expiry_date': forms.TextInput(attrs={
            'class': INPUT_CLASSES            
            }),
            'address': forms.Textarea(attrs={
            'class': INPUT_CLASSES
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('name', 'description', 'price', 'image', 'is_sold')
        name=forms.CharField(widget=forms.TextInput(attrs={
                'placeholder': 'Enter name',
                'class': 'w-full py-4 px-6 rounded-xl'
            }), validators=[validate_name])
        description=forms.CharField(
               widget=forms.TextInput(attrs={
               'placeholder': 'Enter details here',
               'class': 'w-full px-6 py-4 rounded-xl border'
          }), validators=[validate_description])
        price = forms.FloatField(
            min_value=0, max_value= 999999,
            widget=forms.NumberInput(
                attrs={'step': "0.01"}
                ), validators=[validate_price]
                ) 
        widgets={
            'name': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
            'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
            'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
            'class': INPUT_CLASSES
            })
        }