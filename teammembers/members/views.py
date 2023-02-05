from django.shortcuts import render, redirect
from .models import Members

# Create your views here.

def index(request):
    members = Members.objects.all()
    count = len(members)
    return render(request, 'index.html', {'members': members})


def addMember(request):
    if request.method == 'POST':
        new_member = Members(
            first_name = request.POST['firstname'],
            last_name = request.POST['lastname'],
            email = request.POST['emailaddress'],
            phone_number = request.POST['phonenumber'],
            role = request.POST['role']
        )
        new_member.save()
        return redirect('/')

    return render(request, 'add.html')


def editMember(request, pk):
    member = Members.objects.get(id=pk)
    if request.method == 'POST':
        if "update" in request.POST:
            member.first_name = request.POST['firstname']
            member.last_name = request.POST['lastname']
            member.email = request.POST['emailaddress']
            member.phone_number = request.POST['phonenumber']
            member.role = request.POST['role']
            member.save()
            return redirect('/')

        if "delete" in request.POST:
            member.delete()
            return redirect('/')

    return render(request, 'contact-profile.html', {'member': member})

