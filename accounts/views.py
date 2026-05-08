from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm

def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Votre compte a été créé avec succès.")
            return redirect("profile")
    else:
        form = RegisterForm()
    return render(request, "registration/signup.html", {"form": form})

@login_required
def profile(request):
    return render(request, "registration/profile.html")

@login_required
def cart(request):
    # Exemple de panier statique pour démonstration
    cart_items = [
        {"name": "Produit exemple", "price": 99.99, "quantity": 1},
    ]
    total = sum(item["price"] * item["quantity"] for item in cart_items)
    return render(request, "registration/cart.html", {
        "cart_items": cart_items,
        "total": total,
    })