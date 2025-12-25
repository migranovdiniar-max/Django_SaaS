from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model


User = get_user_model()


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username") or None
        password = request.POST.get("password") or None

        if all([username, password]):
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")

    return render(request, "auth/login.html", {})


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username") or None
        email = request.POST.get("email") or None
        password = request.POST.get("password") or None

        # user_exists_qs = User.objects.filter(username__iexact=username).exists()
        # email_exists_qs = User.objects.filter(email__iexact=email).exists()
        try:
            User.objects.create_user(username=username, email=email, password=password)
        except:
            pass

        if all([username, email, password]):
            # Here you would typically create the user
            # For example:
            # user = User.objects.create_user(username=username, email=email, password=password)
            # login(request, user)
            return redirect("/login/")
    return render(request, "auth/register.html", {})
