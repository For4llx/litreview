"""litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import authentification.views
import reviews.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', authentification.views.signup_page, name='signup'),
    path('', authentification.views.LoginPage.as_view(), name='login'),
    path('logout/', authentification.views.logout_user, name='logout'),
    path('feed/', reviews.views.feed, name='feed'),
    path('subscription/', reviews.views.subscription, name='subscription'),
    path(
        'subscription/delete/<int:id>',
        reviews.views.subscription_delete,
        name='subscription_delete'),
    path('post/', reviews.views.post, name='posts'),
    path(
        'post/ticket/create',
        reviews.views.ticket_create,
        name='ticket_create'),
    path(
        'post/ticket/update/<int:id>',
        reviews.views.ticket_update,
        name='ticket_update'),
    path(
        'post/ticket/delete/<int:id>',
        reviews.views.ticket_delete,
        name='ticket_delete'),
    path(
        'post/review/create',
        reviews.views.review_create,
        name='review_create'),
    path(
        'post/review/create/<int:id>',
        reviews.views.review_create,
        name='review_create'),
    path(
        'post/review/update/<int:id>',
        reviews.views.review_update,
        name='review_update'),
    path(
        'post/review/delete/<int:id>',
        reviews.views.review_delete,
        name='review_delete'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
