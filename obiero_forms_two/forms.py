from django import forms


class UserReg(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField()


class PeopleReg(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)


class stud_reg(forms.Form):
    name = forms.CharField(max_length=100)
    gender = forms.CharField(max_length=100)
    school = forms.CharField(max_length=100)
    parent = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=100)
