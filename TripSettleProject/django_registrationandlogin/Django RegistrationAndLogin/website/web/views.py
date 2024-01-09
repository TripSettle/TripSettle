from django.shortcuts import render, redirect, HttpResponseRedirect
<<<<<<< HEAD
from .models import Member,MyModel

=======
from .models import Member


from django.shortcuts import render
from .forms import MyModelForm
>>>>>>> e3ab29cac93c0fc1344c972cf683e66c522efb93
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
            request.session['username'] = member.username
            return render(request, 'web/home.html', {'username': member.username})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'web/login.html', context)
    elif request.method == 'GET':
        username = request.session.get('username', None)
        if username is not None:
            return render(request, 'web/home.html', {'username': username})
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
<<<<<<< HEAD
        form = MyModel(date='08/01/2024', group_name=request.POST['groupname'],  person=request.POST['person'], expenditure=request.POST['expenditure'])
        form.save()
        username = request.session.get('username', None)
        return render(request,'web/home.html',{'username': username})
    else:
        return render(request, 'web/add-grp.html')
    
def viewgroups(request):
    queryset = MyModel.objects.all()
    # MyModel.objects.all().delete()
    return render(request, 'web/viewgroups.html', {'data': queryset})

def addtransaction(request):
    return render(request, 'web/addtransactions.html')
    
def viewhistory(request):
    return render(request, 'web/viewhistory.html')
    
def about(request):
    return render(request, 'web/about.html')
=======
        form = MyModelForm(request.POST)
        if form.is_valid():
            # Handle form submission if needed
            pass
    else:
        form = MyModelForm()

    return render(request, 'web/my_template.html', {'form': form})

>>>>>>> e3ab29cac93c0fc1344c972cf683e66c522efb93

def help(request):
    return render(request, 'web/help.html')



