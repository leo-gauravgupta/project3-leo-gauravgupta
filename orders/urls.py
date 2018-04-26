from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("menuindex/", views.menuindex, name="menuindex"),
    path("order/", views.order, name="order"),
    path("orderplace/", views.orderplace, name="orderplace")
]
