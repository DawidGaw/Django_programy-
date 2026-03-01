from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserRegistrationForm

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if not hasattr(user, 'profile'):
                user.profile = Profile.objects.create(
                    user=user,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    email=user.email
                )
            username = form.cleaned_data.get('username')
            messages.success(request, f'Dear {username}, you have been successfully signed up!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user3/register.html', {'form': form})

@login_required
def dashboard_view(request):
    user = request.user
    profile = user.profile
    context = {
        'username': user.username,
        'date_joined': user.date_joined.strftime('%m/%d/%Y'),
        'last_failed_login': profile.last_failed_login
    }
    return render(request, 'user3/dashboard.html', context)

