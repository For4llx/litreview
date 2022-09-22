from django import forms
from reviews.models import Ticket, Review


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'description', 'image')

class ReviewForm(forms.ModelForm):
    class Meta:
      model = Ticket
      fields = ('title', 'description', 'image')

    class Meta:
        model = Review
        fields = ('headline', 'rating', 'body')
