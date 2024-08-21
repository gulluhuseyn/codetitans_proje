# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import get_user_model 


# class RegisterForm(UserCreationForm):
#     username=forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter email-username", "class": "form-control"}))
#     surname=forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter email-username", "class": "form-control"}))
#     email=forms.CharField(widget=forms.EmailInput(attrs={"placeholder": "Enter email-address", "class": "form-control"}))
#     password=forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"placeholder": "Enter password", "class": "form-control"}))
    
#     class Meta:
#         model = get_user_model()
#         fields = ["username","surname","email", "password"]



from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30)
    surname = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(max_length=10 , widget= forms.PasswordInput)
    
    def clean_email(self):
        username = self.cleaned_data['username']
        surname = self.cleaned_data['surname']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not email.endswith('@example.com'):
            raise forms.ValidationError('Please use an @example.com email address.')

        
        values = {
            "username":username,
            "password":password
        }
        return values
    


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=10 , widget= forms.PasswordInput)