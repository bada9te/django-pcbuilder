from django.urls import path
from . import views

urlpatterns = [
    # content
    path('', view=views.index, name='index'),
    path('setup/', view=views.setup, name='setup'),

    # auth
    path('sign-in/', view=views.login_user, name='sign-in'),
    path('sign-up/', view=views.register_user, name='sign-up'),
    path('logout/', view=views.logout_user, name='logout'),
]
