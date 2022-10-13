from itertools import chain
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from reviews.forms import TicketForm, ReviewForm, SearchUserForm
from reviews.models import Review, Ticket, UserFollows
from authentification.models import User


now = datetime.now()
current_time = now.strftime("%H:%M, %d %m %y")


@login_required
def feed(request):
    """display all posts"""
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    posts = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True
    )
    context = {'posts': posts}
    return render(request, 'reviews/feed.html', context)


def post(request):
    """display all posts of a user"""
    tickets = Ticket.objects.filter(user=request.user)
    reviews = Review.objects.filter(user=request.user)
    posts = sorted(
        chain(tickets, reviews),
        key=lambda instance: instance.time_created,
        reverse=True
    )
    context = {'posts': posts}
    return render(request, 'reviews/post.html', context)


@login_required
def subscription(request):
    """
    Display all subscribers and all subscriptions
    of a user on a GET method.
    """
    search_user_form = SearchUserForm()
    subscriptions = UserFollows.objects.filter(user=request.user)
    subscribers = UserFollows.objects.filter(followed_user=request.user)

    if request.method == 'POST':
        search = request.POST['user']
        followed_user = User.objects.get(username=search)
        new_subscription = UserFollows(
            user=request.user,
            followed_user=followed_user)
        new_subscription.save()
        redirect('subscription')

    context = {
      'search_user_form': search_user_form,
      'subscribers': subscribers,
      'subscriptions': subscriptions
    }
    return render(request, 'reviews/subscription.html', context)


@login_required
def subscription_delete(request, id):
    subscription = UserFollows.objects.get(id=id)
    if request.method == 'POST':
        subscription.delete()
        return redirect('subscription')
    context = {'subscription': subscription}
    return render(request, 'reviews/subscription_delete.html', context)


@login_required
def ticket_create(request):
    """Create a ticket"""
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
        'ticket_form': ticket_form
    }
    return render(request, 'reviews/ticket_create.html', context)


@login_required
def ticket_update(request, id):
    """Update a ticket"""
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
def review_create(request, id=None):
    if id:
        ticket = Ticket.objects.get(id=id)
        review_form = ReviewForm()
        if request.method == 'POST':
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.user = request.user
                review.ticket = ticket
                review.time_created = current_time
                review.save()

                return redirect('feed')
        context = {
            'ticket': ticket,
            'review_form': review_form,
        }
    else:
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
        'review': review,
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
