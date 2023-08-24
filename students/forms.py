from django import forms
from .models import Student 

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Student  
        fields = ['first_name', 'last_name', 'email', 'student_id']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'student_id': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        }
        
class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = Student
        fields = ['username', 'password', 'password_confirm', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError('Passwords do not match!')
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Student.objects.filter(username=username).exists():
            raise forms.ValidationError('Username is already taken. Please choose another one.')
        return username
