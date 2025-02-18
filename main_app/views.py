from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Member, Gear
from .forms import GameForm
from django.contrib.auth.views import LoginView

class Home(LoginView):
    template_name = 'home.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('member-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def about(request):
    return render(request, 'about.html')

@login_required
def member_index(request):
    members = Member.objects.filter(user=request.user)
    return render(request, 'members/index.html', {'members': members})

@login_required
def member_detail(request, member_id):
    member = Member.objects.get(id=member_id)
    gears_member_doesnt_have = Gear.objects.exclude(id__in = member.gears.all().values_list('id'))

    game_form = GameForm()
    return render(request, 'members/detail.html', {
        'member': member,
        'game_form': game_form,
        'gears': gears_member_doesnt_have
    })

@login_required
def add_game(request, member_id):
    form = GameForm(request.POST)
    if form.is_valid():
        new_game = form.save(commit=False)
        new_game.member_id = member_id
        new_game.save()
    return redirect('member-detail', member_id=member_id)

@login_required
def associate_gear(request, member_id, gear_id):
    Member.objects.get(id=member_id).gears.add(gear_id)
    return redirect('member-detail', member_id=member_id)

@login_required
def remove_gear(request, member_id, gear_id):
    m = Member.objects.get(id=member_id)
    g = Gear.objects.get(id=gear_id)
    m.gears.remove(g)
    return redirect('member-detail', member_id=member_id)

class MemberCreate(LoginRequiredMixin, CreateView):
    model = Member
    fields = ['name', 'age', 'gender', 'dupr']
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class MemberUpdate(LoginRequiredMixin, UpdateView):
    model = Member
    fields = ['age', 'gender', 'dupr']

class MemberDelete(LoginRequiredMixin, DeleteView):
    model = Member
    success_url = '/members/'

class GearCreate(LoginRequiredMixin, CreateView):
    model = Gear
    fields = '__all__'

class GearList(LoginRequiredMixin, ListView):
    model = Gear
    
class GearDetail(LoginRequiredMixin, DetailView):
    model = Gear

class GearUpdate(LoginRequiredMixin, UpdateView):
    model = Gear
    fields = ['name', 'color']

class GearDelete(LoginRequiredMixin, DeleteView):
    model = Gear
    success_url = '/gears/'