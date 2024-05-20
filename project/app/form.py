from django import forms

from app.models import Author, BlogPost, UserAuthentication
class FormView(forms.ModelForm):
    class Meta:
        model= BlogPost
        fields = (
            '__all__'
        )
class FormViewAuthor(forms.ModelForm):
    class Meta:
        model= Author
        fields = (
            '__all__'
        )

class FormViewAut(forms.ModelForm):
    class Meta:
        model= UserAuthentication
        fields = (
            '__all__'
        )

class FormViewLog(forms.ModelForm):
    class Meta:
        model= UserAuthentication
        fields = (
            '__all__'
        )