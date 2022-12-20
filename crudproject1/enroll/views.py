from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.


# This function will add new item and show all items
def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            return HttpResponseRedirect('/thanks/')
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form':fm,'stu':stud})


# Landing Page for httpresopnseredirect
def thanks(request):
    return render(request, 'enroll/thanks.html')



# This function will Update/Edit
def update_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            # fm.save()
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            upd = User(id=id, name=nm, email=em, password=pw)
            upd.save()
            return HttpResponseRedirect('/thanks/')
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)        
    return render(request, "enroll/updatestudent.html", {'form':fm})



# THis function will delete
def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')