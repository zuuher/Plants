from django.shortcuts import render, redirect ,get_object_or_404
from .forms import PlantForm, SignupForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from .models import Plant, user as UserModel


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if User.objects.filter(email=email).exists():
                messages.error(request, "هذا البريد مسجل مسبقًا")
                return render(request, 'signup.html', {'form': form})

            # إنشاء مستخدم جديد
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "تم إنشاء الحساب بنجاح، يمكنك تسجيل الدخول الآن")
            return redirect('login')
        else:
            messages.error(request, "يرجى تصحيح الأخطاء في النموذج")
    else:
        form = SignupForm()
    
    return render(request, 'signup.html', {'form': form})

   
def LOGIN(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "البريد غير موجود، الرجاء إنشاء حساب جديد (Signup)")
            return render(request, 'LOGIN.html')

        user = authenticate(request, username=user_obj.username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "تم تسجيل الدخول بنجاح!")
            return redirect('home')
        else:
            messages.error(request, "كلمة السر خاطئة.")
            return render(request, 'LOGIN.html')

    return render(request, 'LOGIN.html')

def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')  # أو أي صفحة تريد إعادة التوجيه لها
@login_required(login_url='login')
def home(request):
    plants = Plant.objects.all()
    return render(request, "home.html", {'plants': plants})
@login_required(login_url='login')
def about(request):
    return render(request, "about.html") 
@login_required(login_url='login')
def details(request, plan_id):
    plant = get_object_or_404(Plant, pk=plan_id)
    return render(request, 'details.html', {'plant': plant})

@login_required(login_url='login')
def add_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            plant = form.save()
            messages.success(request, "Plant added successfully.")
            return redirect('home')
        else:
            messages.error(request, "Error while saving plant. Please check the form.")
    else:
        form = PlantForm()
    return render(request, 'plant.html', {'form': form})
@login_required(login_url='login')
def edit_plant(request, plan_id):
    plant = get_object_or_404(Plant, pk=plan_id)

    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            messages.success(request, "Plant updated successfully.")
            return redirect('home')
        else:
            messages.error(request, "Error while updating plant. Please check the form.")
    else:
        form = PlantForm(instance=plant)

    return render(request, 'details.html', {'form': form, 'plant': plant})


@login_required(login_url='login')
def delete_plant(request, plan_id):
    plant = get_object_or_404(Plant, pk=plan_id)
    plant.delete()
    messages.success(request, f"Plant '{plant.name}' has been deleted successfully.")
    return redirect('home')
