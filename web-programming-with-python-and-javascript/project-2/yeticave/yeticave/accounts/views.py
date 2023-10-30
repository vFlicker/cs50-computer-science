from django.contrib.auth import get_user_model, login as auth_login
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.urls import reverse

from .forms import UserCreationForm

User = get_user_model()


@require_http_methods(["GET", "POST"])
def register(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = UserCreationForm()
        return render(request, "registration/register.html", {"form": form})

    if (form := UserCreationForm(request.POST)).is_valid():
        user = form.save()
        auth_login(request, user)
        return HttpResponseRedirect(reverse("index"))

    return render(request, "registration/register.html", {"form": form})