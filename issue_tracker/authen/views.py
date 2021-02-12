from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import user_passes_test
from .forms import SignUpForm,question,askquestion
from .models import questions,askquestions
from django.db.models import Count
from django.views.generic import ListView
from .filters import OrderFilter
from .models import CustomUser,questions
from .models import askquestions as ask


 
def home(request):
    '''labels=[]
    data=[]
    queryset=questions.objects.values('category').annotate(total=Count('category'))
    for i in queryset:
        labels.append(i['category'])
        data.append(i.['total']){'labels':labels,'data':data,}'''
    sup_count=2
    user_count=CustomUser.objects.count()-sup_count
    que_count=questions.objects.count()
    unans_count=ask.objects.count()


    return render(request, 'home.html',{'user_count':user_count,'que_count':que_count,'sup_count':sup_count,'unans_count':unans_count})
 
 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', { 'form' : form })
   


def allquestions(request):
    context={}
    que=questions.objects.all()

    myFilter=OrderFilter(request.GET, queryset=que)
    que = myFilter.qs
    if que:
        context={'dataset':que,'myFilter':myFilter}
        return render(request, 'allquestions.html',context)
    else:
        return render(request,'noresults.html')


def addquestion(request):
    if request.user.is_superuser:
        context={}

        form=question(request.POST or None)
        if form.is_valid():
            form.save()
        context['form']=form
        return render(request,'addquestion.html',context)
    else:
        return render(request,'noaccess.html')

def askquestions(request):
    context={}

    form=askquestion(request.POST or None)
    if form.is_valid():
        form.save()
    context['form']=form
    return render(request,'askquestions.html',context)