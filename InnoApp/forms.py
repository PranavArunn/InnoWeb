
from .models import New_feedback, New_model
from django.forms import ModelForm, TextInput
class New_Form(ModelForm):
    class Meta:
        model = New_model
        fields = ["Word"]
        widgets = {"Word":TextInput(attrs={"class":"input","placeholder":"#Writetopic"})}

class New_Form1(ModelForm):
    class Meta:
        model = New_model
        fields = ["Word","Content"]
        widgets = {"Word":TextInput(attrs={"class":"input","placeholder":"#Writetopic"}),
        "Content":TextInput(attrs={"class":"input","placeholder":"#Writecontent"})}

class New_form2(ModelForm):
    class Meta:
        model = New_feedback
        fields = ["feedback1", "feedback2"]
        widgets = {"feedback1":TextInput(attrs ={"class":"input","placeholder":"#Writetopic"}),
        "feedback2":TextInput(attrs={"class":"input","placeholder":"#Writetopic"})}
        

