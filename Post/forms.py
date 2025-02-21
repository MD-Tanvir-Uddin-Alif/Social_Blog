from django import forms
from .import models

class Post_Create_Form(forms.ModelForm):
    class Meta:
        model = models.Post_Model
        fields = ['title','content']


class Update_Post_Form(forms.ModelForm):
    class Meta:
        model = models.Post_Model
        fields = ['title','content']


class Comment_Form(forms.ModelForm):
    class Meta:
        model = models.Comment_Model
        fields = ['content']