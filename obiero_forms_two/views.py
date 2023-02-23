from django.shortcuts import render

from .forms import UserReg

from .forms import PeopleReg

from .forms import stud_reg


def reg(request):
    submit_button = request.POST.get("Register")
    name = ''
    email = ''
    password = ''

    regForm = UserReg(request.POST or None)
    if regForm.is_valid():
        name = regForm.cleaned_data.get("name")
        email = regForm.cleaned_data.get("Email")
        password = regForm.cleaned_data.get("Password")

    context = {'regForm': regForm,
               'name': name,
               'email': email,
               'submit_button': submit_button
               }

    return render(request, 'Register.html', context)


def reg_people(request):
    submit_people_button = request.POST.get("peoplebtn")
    name = ''
    age = ''
    phone = ''
    city = ''

    people_form = PeopleReg(request.POST or None)
    if people_form.is_valid():
        name = people_form.cleaned_data.get("name")
        age = people_form.cleaned_data.get("age")
        phone = people_form.cleaned_data.get("phone")
        city = people_form.cleaned_data.get("city")

    context = {'people_form':people_form,
               'name': name,
               'age': age,
               'phone': phone,
               'city': city,
               'submit_people_button': submit_people_button
               }
    return render(request, 'people.html', context)


def reg_students(request):
    submit_student_button = request.POST.get("studentbtn")
    name = ''
    gender = ''
    school = ''
    parent = ''
    phone_number = ''

    student_form = stud_reg(request.POST or None)
    if student_form.is_valid():
        name = student_form.cleaned_data.get("name")
        gender = student_form.cleaned_data.get("gender")
        school = student_form.cleaned_data.get("school")
        parent = student_form.cleaned_data.get("parent")
        phone_number = student_form.cleaned_data.get("phone_number")

    context = {'student_form': student_form,
               'name': name,
               'gender': gender,
               'school': school,
               'parent': parent,
               'phone_number': phone_number,
               'submit_student_button': submit_student_button
               }
    return render(request, 'student.html', context)
