from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Member


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def member_index(request):
    members = Member.objects.all()
    return render(request, 'members/index.html', {'members': members})

def member_detail(request, member_id):
    member = Member.objects.get(id=member_id)
    return render(request, 'members/detail.html', {'member': member})

class MemberCreate(CreateView):
    model = Member
    fields = '__all__'

class MemberUpdate(UpdateView):
    model = Member
    fields = ['age', 'gender', 'dupr']

class MemberDelete(DeleteView):
    model = Member
    success_url = '/members/'
