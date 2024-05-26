from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from django.views import View
from .forms import loginForm, registerForm, randecodeForm, AddressCreationForm,EditForm
from random import randint
import ghasedakpack
from .models import user_otp, User,Contact
#from django.utils.crypto import get_random_string
from uuid import uuid4

SMS = ghasedakpack.Ghasedak("383e7d07eb016594710504710ad3856d5ffdb2ba2b3287edcce4af327428e9f7")


class UserLogin(View):
    def get(self, request):
        form = loginForm()
        return render(request, "account/login.html", {"form": form})

    def post(self, request):
        form = loginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error("Phone", "is valid data")
        else:
            form.add_error("Phone", "is valid")
        return render(request, 'account/login.html', {"form": form})


class registerView(View):
    def get(self, request):
        form = registerForm()
        return render(request, "account/register.html", {"form": form})

    def post(self, request):
        form = registerForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            randcode = randint(1000, 9999)
            SMS.verification(
                {'receptor': cd["Phone"], 'type': '1', 'template': 'shoppingahmad', 'param1': randcode}
            )
            token = str(uuid4())
            user_otp.objects.create(Phone=cd["Phone"], code=randcode, token=token)
            print(randcode)
            return redirect(reverse("account:randecode") + f'?token={token}')
        else:
            form.add_error("Phone", "is valid")
        return render(request, 'account/register.html', {"form": form})


class randecodeView(View):
    def get(self, request):
        form = randecodeForm()
        return render(request, "account/randecode.html", {"form": form})

    def post(self, request):
        token = request.GET.get("token")
        form = randecodeForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if user_otp.objects.filter(code=cd["code"], token=token).exists():
                otp = user_otp.objects.get(token=token)
                user, is_create = User.objects.get_or_create(Phone=otp.Phone)
                # user.backend ="django.contrib.auth.backends.ModelBackend"
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                otp.delete()
                return redirect("/")
            else:
                form.add_error("Phone", "Phone is valid")
        else:
            form.add_error("Phone", "is valid")
        return render(request, 'account/randecode.html', {"form": form})


class AddAddressView(View):
    def post(self, request):
        form = AddressCreationForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)

            return render(request, 'account/Addaddress.html', {'form': form})

    def get(self, request):
        form = AddressCreationForm()
        return render(request, 'account/Addaddress.html', {'form': form})

def ContacView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(name=name,email=email,subject=subject,message=message)
        return render(request,'account/contact.html',{})

    return render(request,'account/contact.html',{})


def Edit(request):
    user = request.user
    form = EditForm(instance=user)
    if request.method == 'POST':
        form = EditForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'account/edit_profile.html',{'form':form})
def user_logout(request):
    logout(request)
    return redirect('/')



