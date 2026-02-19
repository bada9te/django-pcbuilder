from django.urls import path
from . import views

urlpatterns = [
    # content
    path('', view=views.index, name='index'),
    path('setup/', view=views.setup, name='setup'),
    path('profile/', view=views.profile, name='profile'),

    # auth
    path('account_login/', view=views.login_user, name='account_login'),
    path('sign-up/', view=views.register_user, name='sign-up'),
    path('logout/', view=views.logout_user, name='logout'),
]
