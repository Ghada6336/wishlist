
from django.shortcuts import render, redirect
#from .models import
from .models import  Item ,NewItem
from .forms import SignupForm ,SigninForm ,CreateForm
from django.contrib.auth import login, authenticate, logout

def home(request):
    return render(request, 'home.html', {'msg':'WISHLIST'})

def list(request):
    context = {
        "items":Item.objects.all()
    }
    return render(request, 'list.html', context)


def detail(request, item_id):
    items = Item.objects.get(id=item_id)
    new = NewItem.objects.filter(new=new)
    context = {
        "items": items,
        "new": new,
    }
    return render(request, 'detail.html', context)



def create(request):
    form = CreateForm()
    if request.method == "POST":
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            items= form.save(commit=False)
            items.new = request.user
            items.save()
            return redirect('list')
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)

def update(request, item_id):
    item = Item.objects.get(id=item_id)
    form = CreateForm(instance=item)
    if request.method == "POST":
        form = CreateForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        "item": item,
        "form":form,
    }
    return render(request, 'update.html', context)

def delete(request, item_id):

    item = Item.objects.get(id=item_id)
    item.delete()
    return redirect('list')

def item_create(request, item_id):
    form = ItemForm()

    dr = Item.objects.get(id=item_id)

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.item = dr
            item.save()
            return redirect('detail', item_id)
    context = {
        "form":form,
        "item": item,
    }
    return render(request, 'item_create.html', context)



def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            return redirect("signin")
    context = {
        "form":form,
    }
    return render(request, 'signup.html', context)


def signin(request):
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)

            if auth_user is not None:
                login(request, auth_user)
                return redirect('list')
    context = {
        "form":form
    }
    return render(request, 'signin.html', context)


def signout(request):
    logout(request)
    return redirect("home")
