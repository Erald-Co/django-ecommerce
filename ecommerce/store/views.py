from django.shortcuts import render

def store(request): # definisi masing2 fungsi
    context = {}
    return render(request, 'store/store.html', context)

def cart(request): # definisi masing2 fungsi
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request): # definisi masing2 fungsi
    context = {}
    return render(request, 'store/checkout.html', context)
