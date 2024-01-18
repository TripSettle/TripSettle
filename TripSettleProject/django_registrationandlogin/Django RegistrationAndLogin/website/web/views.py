from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Member,MyModel,AddTransaction
from django.core.mail import send_mail

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
        
def addgroup(request):
    if request.method == 'POST':
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
    queryset = AddTransaction.objects.all()
    return render(request, 'web/addtransactions.html',{'data':queryset})

def settleup(request):
    return render(request, 'web/settleup.html')
    
def viewhistory(request):
    return render(request, 'web/viewhistory.html')
    
def about(request):
    return render(request, 'web/about.html')

def help(request):
    return render(request, 'web/help.html')

def sendemail(request):
    if request.method == 'GET':
        subject = 'Subject of the Email'
        message = 'Body of the Email'
        from_email = 'yourmail@gmail.com'
        recipient_list = ['mymail@gmail.com']
        send_mail(subject, message, from_email, recipient_list)

        username = request.session.get('username', None)
        return render(request,'web/home.html',{'username': username})
    else:
        return render(request, 'web/settleup.html')

def filltransaction(request):
    li=["dhaya","hari","John"]
    if request.method == 'POST':
        form = AddTransaction(transname=request.POST['transname'], amtspent=request.POST['amtspent'],  personName=request.POST['personName'])
        form.save()
        queryset = AddTransaction.objects.all()
        return render(request,'web/addtransactions.html',{'data':queryset})
    return render(request, 'web/filltransaction.html',{"mylist":li})

