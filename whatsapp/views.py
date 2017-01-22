from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.utils import timezone
from .models import Message
from .forms import MessageForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.
@login_required
def index(request: HttpRequest):
    users_list = User.objects.exclude(id=request.user.id)
    context = {"users_list": users_list}
    return render(request, "whatsapp/index.html", context)


@login_required
def chat(request: HttpRequest, receiver_id: int):
    receiver = get_object_or_404(User, id=receiver_id)
    sender = request.user

    if request.method == "POST":
        message = Message(sender=sender, receiver=receiver, text=request.POST.get("text"), pub_date=timezone.now())
        message.save()
        return redirect(message)

    message_list = Message.objects.filter(Q(sender=sender, receiver=receiver) |
                                          Q(sender=receiver, receiver=sender)).order_by("pub_date")
    form = MessageForm()
    context = {"message_list": message_list, "form": form, "receiver": receiver}
    return render(request, "whatsapp/chat.html", context)


def registration(request: HttpRequest):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/whatsapp")
    else:
        form = UserRegistrationForm()

    return render(request, "registration/registration.html", {'form': form})
