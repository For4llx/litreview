from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from reviews.forms import TicketForm
from reviews.models import Review, Ticket


now = datetime.now()
current_time = now.strftime("%H:%M, %d %m %y")

@login_required
def flow(request):
    reviews = Review.objects.all().order_by('time_created')
    tickets = Ticket.objects.all().order_by('time_created')
    context = {'reviews': reviews, 'tickets': tickets}
    return render(request, 'reviews/flow.html', context)

@login_required
def createTicket(request):
    ticket_form = TicketForm()
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.time_created = current_time
            ticket.save()

            return redirect('flow')
    context = {
        'ticket_form': ticket_form,
    }
    return render(request, 'reviews/create_ticket.html', context)