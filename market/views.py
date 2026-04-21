from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RegisterForm, SkillForm
from .models import Skill


def home(request):
    """Show the public list of available skill posts."""
    skills = Skill.objects.order_by('-created_at')
    return render(request, 'market/home.html', {'skills': skills})


def skill_detail(request, pk):
    """Show the details of a single skill post."""
    skill = get_object_or_404(Skill, pk=pk)
    return render(request, 'market/skill_detail.html', {'skill': skill})


@login_required
def dashboard(request):
    """Show the signed-in user's own skill posts."""
    skills = request.user.skills.order_by('-created_at')
    return render(request, 'market/dashboard.html', {'skills': skills})


@login_required
def skill_create(request):
    """Create a new skill post and save it for the owner."""
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = request.user
            skill.save()
            messages.success(request, 'Your skill post was created.')
            return redirect('market:dashboard')
    else:
        form = SkillForm()
    return render(request, 'market/skill_form.html', {'form': form, 'page_title': 'Create Skill Post'})


@login_required
def skill_update(request, pk):
    """Update an existing skill post owned by the signed-in user."""
    skill = get_object_or_404(Skill, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your skill post was updated.')
            return redirect('market:dashboard')
    else:
        form = SkillForm(instance=skill)
    return render(request, 'market/skill_form.html', {'form': form, 'page_title': 'Edit Skill Post'})


@login_required
def skill_delete(request, pk):
    """Delete a skill post owned by the signed-in user."""
    skill = get_object_or_404(Skill, pk=pk, owner=request.user)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, 'Your skill post was deleted.')
        return redirect('market:dashboard')
    return render(request, 'market/skill_confirm_delete.html', {'skill': skill})


def register(request):
    """Register a new user account and log the user in."""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully.')
            return redirect('market:home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})
