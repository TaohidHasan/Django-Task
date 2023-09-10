from django import forms  
from website.models import Stock  
class StockForm(forms.ModelForm):  
    def __str__(self):
        return self.name
    
    class Meta:  
        model = Stock  
        fields = [ 'date','Trade','High','Low', 'Open', 'Close', 'Volume'] 
        widgets = { 'date': forms.DateInput(attrs={ 'class': 'form-control' }), 
            'Trade': forms.TextInput(attrs={ 'class': 'form-control' }),
            'High': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'Low': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'Open': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'Close': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'Volume': forms.NumberInput(attrs={ 'class': 'form-control' }),

      }