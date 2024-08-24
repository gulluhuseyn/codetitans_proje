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
            "email":email,
            "password":password
        }
        return values
    


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=10 , widget= forms.PasswordInput)