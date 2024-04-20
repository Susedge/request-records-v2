from django import forms
from .models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserRegistrationForm(forms.ModelForm):
    student_number = forms.CharField(max_length=64)

    class Meta:
        model = User
        fields = ['email', 'student_number', 'password']

    def save(self, commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data["password"])

        if commit == True:
            user.save()
        return user


# For modifying user form
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'student_number', 'is_admin')

    def clean_password(self):
        return self.initial["password"]