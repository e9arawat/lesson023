"""
    Module name :- forms
    Classes :- StudentForm, TeacherForm
"""

from django import forms


class StudentForm(forms.Form):
    """
    Form for Student registration.
    """

    name = forms.CharField(max_length=50)
    age = forms.IntegerField()
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=15)

    name.widget.attrs.update({"class": "form-control"})
    age.widget.attrs.update({"class": "form-control"})
    email.widget.attrs.update({"class": "form-control"})
    phone_no.widget.attrs.update({"class": "form-control"})


class TeacherForm(forms.Form):
    """
    Form for Teacher registration.
    """

    name = forms.CharField(max_length=50)
    age = forms.IntegerField()
    email = forms.EmailField()
    phone_no = forms.CharField(max_length=15)
    experience = forms.IntegerField()

    name.widget.attrs.update({"class": "form-control"})
    age.widget.attrs.update({"class": "form-control"})
    email.widget.attrs.update({"class": "form-control"})
    phone_no.widget.attrs.update({"class": "form-control"})
    experience.widget.attrs.update({"class": "form-control"})
