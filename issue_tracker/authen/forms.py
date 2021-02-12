from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import Form,ChoiceField
from .models import CustomUser,questions,askquestions
 
 
class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, help_text='Required. 100 charaters or fewer.', )
 
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('full_name', 'age',)

class question(forms.ModelForm):
    question=forms.CharField(widget=forms.Textarea,required=True)
    class Meta:
        model=questions
        fields=[
            "category",
            "question",
            "answer",
        ]

class askquestion(forms.ModelForm):
    question=forms.CharField(widget=forms.Textarea,required=True)
    class Meta:
        model=askquestions
        fields=[
            "category",
            "question",
        ]