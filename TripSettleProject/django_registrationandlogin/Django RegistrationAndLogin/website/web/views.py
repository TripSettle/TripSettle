from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Member


from django.shortcuts import render
from .forms import MyModelForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], password=request.POST['password'],  firstname=request.POST['firstname'], lastname=request.POST['lastname'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'web/index.html')

def login(request):
    return render(request, 'web/login.html')

def home(request):
    member = None
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'web/home.html', {'member': member})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'web/login.html', context)
    elif request.method == 'GET':
        if member is not None:
            return render(request, 'web/home.html', {'member': member})
        else:
            context = {'msg': 'Session Expired'}
            return render(request, 'web/login.html', context)

# myapp/views.py


def my_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            # Handle form submission if needed
            pass
    else:
        form = MyModelForm()

    return render(request, 'web/my_template.html', {'form': form})

        
def addgroup(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            # Handle form submission if needed
            pass
    else:
        form = MyModelForm()

    return render(request, 'web/my_template.html', {'form': form})





