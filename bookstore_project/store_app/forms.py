from django import forms
from .models import AuthorModel,BookModel,ReviewModel

class AuthorForm(forms.ModelForm):
    class Meta:
        model = AuthorModel
        fields = "__all__"

class BookForm(forms.ModelForm):
    publication_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    class Meta:
        model = BookModel
        fields = "__all__"

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = ('content','rating',)