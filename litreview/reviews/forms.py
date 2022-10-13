from django import forms
from reviews.models import Ticket, Review


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'description', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form__title'}),
            'description': forms.Textarea(attrs={'class': 'form__description'})
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('headline', 'rating', 'body')
        labels = {
            'headline': 'Titre',
            'rating': 'Note',
            'body': 'Commentaire'}


class SearchUserForm(forms.Form):
    user = forms.CharField(label='', max_length=100)
