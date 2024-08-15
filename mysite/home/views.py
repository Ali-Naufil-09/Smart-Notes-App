from django.shortcuts import render
from django.http import HttpResponse
#from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,CreateView
#from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.

from django.contrib.auth.forms import UserCreationForm #creating a form using django


from django.shortcuts import redirect

class LoginInterfaceView(LoginView):
   template_name='home/login.html'

class LogoutInterfaceView(LogoutView):
    template_name='home/logout.html'
    
#method 1: (old method)
#def home(request):
#    return render(request,'home/welcome.html',{'today':datetime.today()})  #demostration of how to add dates # now we can add the date today by just writing today

#method 2:
class HomeView(TemplateView):
    template_name='home/welcome.html'



class SignupView(CreateView):
    form_class=UserCreationForm
    template_name='home/register.html'
    success_url='/smart/notes'
#the below function ensures that a loggedin user can never access the signup form(page)
    def get(self,request,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request,*args,**kwargs)
        


#method 1:
#@login_required(login_url='/admin') #in case a restricted user accesses authorized page he will redirect to authetification page
#def authorized(request):
 #   return render(request,'home/authorized.html',{})


#method 2:
#class AuthorizedView(LoginRequiredMixin,TemplateView):
 #   template_name='home/authorized.html'
  #  login_url='/admin'