from django import forms
from .models import Genre, Movie, Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content', 'score',)