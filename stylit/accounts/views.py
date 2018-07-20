from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views import View
from .models import Account
from gallery.models import Meme
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,logout,login
from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
import json
from .forms import SignUpForm

# Create your views here.

def signup(request):
    args = {}
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            #print('hello')
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            account = Account(user=user)
            account.save()
            login(request, user)
            return redirect('/gallery/index')

    else:
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form': form})

    args['form'] = form
    return render(request, 'accounts/signup.html', args)

def wallview(request,username):
    currentuser = get_object_or_404(User,username=username)

    if(request.user.username != currentuser.username):
        return HttpResponseRedirect('/gallery/index')

    user_followed = currentuser.profile.following.all()
    memes = Meme.objects.filter(author__in = user_followed)
    return render(request, 'accounts/wall.html', {'memes': memes})


def portfolioview(request,username):
    user = get_object_or_404(User,username=username)
    memes = Meme.objects.filter(author__username=username)
    return render(request,'accounts/portfolio.html',{'memes':memes,'profile_user':user})

def followview(request,username):
    user = get_object_or_404(User,username=username)
    if(request.user.is_authenticated):
        if user in request.user.profile.following.all():
            request.user.profile.following.remove(user)
            followed = False
        else:
            request.user.profile.following.add(user)
            followed = True
        return HttpResponse(json.dumps({'followed': followed, 'following': user.profile.following.all().count(),'followers':user.followers.all().count()}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'notlogedin': True}), content_type="application/json")

