from django import forms

class ContactForm(forms.Form):
   #  COUNTRIES = [
   #     ('CL', 'Chile'),
   #     ('VE', 'Venezuela'),
   #     ('AR', 'Argentina'),
   #     ('US', 'E.E.U.U')
   #     ]
   # # Agregar los campos del formulario
   #  name = forms.CharField(label='Nombre', max_length=400)
   #  email = forms.EmailField()
   #  age = forms.IntegerField(min_value=1)
   #  country = forms.ChoiceField(choices=COUNTRIES)
   #  country_extra = forms.MultipleChoiceField(choices=COUNTRIES)
   email = forms.EmailField(
       widget=forms.TextInput(attrs={
           'class':'form-control',
           'placeholder': 'example@gmail.com'
           })
       )
   comment = forms.CharField(
       widget=forms.Textarea(attrs={
           'class':'form-control',
           'rows': 3           
           })
       )
   firstName = forms.CharField(
       widget=forms.TextInput(attrs={
           'class':'form-control',
           'placeholder': 'First Name'
           })
       )

   lastName = forms.CharField(
       widget=forms.TextInput(attrs={
           'class':'form-control',
           'placeholder': 'Last Name'
           })
       )

