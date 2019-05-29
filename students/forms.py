from django import forms
from .models import Student

class Studentform(forms.ModelForm):
	address = forms.CharField(label="address",widget=forms.Textarea(attrs={'class': 'form-control','rows':'2' ,}))
	class Meta:
		model = Student
		fields = ['pic','name', 'classinfo', 'rollno', 'dob','mothername', 'fathername', 'address', 'mobileno', 'email', 'nationality']
