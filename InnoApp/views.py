
from django.shortcuts import render,HttpResponse
from .models import New_model, New_feedback
from .forms import New_Form, New_Form1, New_form2
from wikipedia import *

def index(request):
    Output = ""
    if request.method == "POST":
        try:
            Search = request.POST["Search"]
            Output = summary(Search)
        except:
            wiki = New_model.objects.all()
            for i in wiki:
                if i.Word == Search:
                    Output = i.Content
                else:
                    return HttpResponse("Invalid data! please enter the correct information")
        return render(request,"InnoApp/Index.html",{"Output":Output})


    return render(request,"InnoApp/Index.html")

def Create(request):
    if request.method == "POST":
        form = New_Form1(request.POST)
        form.save()
    form = New_Form1()
    return render(request,"InnoApp/Edit.html")
    
    


def Feedback(request):
    if request.method == "POST":
        form = New_form2(request.POST)
        form.save()
    form = New_form2()
    return render(request,"InnoApp/Feedback.html")