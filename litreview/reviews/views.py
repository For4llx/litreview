from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from reviews.forms import TicketForm, ReviewForm
from reviews.models import Review, Ticket, UserFollows
from itertools import chain

now = datetime.now()
current_time = now.strftime("%H:%M, %d %m %y")

@login_required
def feed(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    posts = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True
    )
    context = {'posts': posts}
    return render(request, 'reviews/feed.html', context)

def posts(request):
    tickets = Ticket.objects.filter(user = request.user)
    reviews = Review.objects.filter(user = request.user)
    posts = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True
    )
    context = {'posts': posts}
    return render(request, 'reviews/posts.html', context)

@login_required
def subscription(request):
    subscriptions = UserFollows.objects.filter(user = request.user)
    subscribers = UserFollows.objects.filter(followed_user = request.user)
    context = {
      'subscribers': subscribers,
      'subscriptions': subscriptions
    }
    return render(request, 'reviews/subscription.html', context)

@login_required
def ticket_create(request):
    ticket_form = TicketForm()
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.time_created = current_time
            ticket.save()

            return redirect('feed')
    context = {
        'ticket_form': ticket_form,
    }
    return render(request, 'reviews/ticket_create.html', context)

@login_required
def ticket_update(request, id):
    ticket = Ticket.objects.get(id=id)
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, instance=ticket)
        if ticket_form.is_valid():
            ticket_form.save()
            return redirect('feed')
    else:
        ticket_form = TicketForm(instance=ticket)
    context = {
        'ticket_form': ticket_form
    }
    return render(request, 'reviews/ticket_update.html', context)

@login_required
def ticket_delete(request, id):
    ticket = Ticket.objects.get(id=id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('feed')
    context = {'ticket': ticket}
    return render(request, 'reviews/ticket_delete.html', context)

@login_required
def review_create(request):
    ticket_form = TicketForm()
    review_form = ReviewForm()
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if review_form.is_valid() and ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.time_created = current_time
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.time_created = current_time
            review.save()

            return redirect('feed')
    context = {
        'ticket_form': ticket_form,
        'review_form': review_form,
    }
    return render(request, 'reviews/review_create.html', context)

@login_required
def review_update(request, id):
    review = Review.objects.get(id=id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect('feed')
    else:
        review_form = ReviewForm(instance=review)
    context = {
        'review_form': review_form
    }
    return render(request, 'reviews/review_update.html', context)

@login_required
def review_delete(request, id):
    review = Review.objects.get(id=id)
    if request.method == 'POST':
        review.delete()
        return redirect('feed')
    context = {'review': review}
    return render(request, 'reviews/review_delete.html', context)