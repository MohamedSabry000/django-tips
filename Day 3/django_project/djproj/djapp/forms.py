from django import forms
from .models import Student, Track

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('fname', 'lname', 'age', 'student_track')
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'lname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'student_track': forms.Select(attrs={'class': 'form-control'}),
        }
        
class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ('track_name',)
        