from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Enrollment, Subject

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={'placeholder': 'Email'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': None,
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs.update({'placeholder': 'Username'})
        self.fields['password1'].label = ''
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].label = ''
        self.fields['password2'].widget.attrs.update({'placeholder': 'Confirm Password'})

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['full_name', 'course', 'email']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name'}),
            'course': forms.TextInput(attrs={'placeholder': 'Course'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
        }
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_code', 'subject_name', 'instructor', 'room', 'department', 'time']

