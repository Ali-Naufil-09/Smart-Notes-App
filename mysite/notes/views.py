from django.shortcuts import render
from .models import Notes
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from . forms import NotesForm
from django.http import HttpResponseRedirect

#adding security check so that only logged in users can create,edit,delete notes
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
#def list(request):
    #a=Notes.objects.all()
    #return render(request,'notes/notes_list.html' ,{'notes':a})

class NotesListView(LoginRequiredMixin,ListView):
  model=Notes
  context_object_name="notes"
  login_url='/login'
  
  def get_queryset(self):
      return self.request.user.notes.all()  #only loggedin user will have access to notes
  

#def detail(request,pk):
 #   note=Notes.objects.get(pk=pk)
  #  return render(request,'notes/notes_detail.html',{'note':note})
  
class NotesDetailView(LoginRequiredMixin,DetailView):
    model=Notes
    context_object_name="note"  #note is the object name for calling
    login_url='/login'
  
    def get_queryset(self):
      return self.request.user.notes.all()  #only loggedin user will have access to notes
    
class NotesCreateView(LoginRequiredMixin,CreateView):
    model=Notes
  #  fields=['title','text']  #these are the form feilds that i will give to user to fill them and create a note
    success_url='/smart/notes/'  #when the note is created it will go to notes url
    form_class=NotesForm 
    login_url='/login'
  
    def form_valid(self,form):
      self.object=form.save(commit=False)
      self.object.user=self.request.user
      self.object.save()
      return HttpResponseRedirect(self.get_success_url())  #this function asks user that he has registered or not
      
    
    
class NotesUpdateView(LoginRequiredMixin,UpdateView):
    model=Notes
    success_url= '/smart/notes/' 
    form_class=NotesForm   
    login_url='/login'
  
    def get_queryset(self):
      return self.request.user.notes.all()  #only loggedin user will have access to notes
      
      
    
class NotesDeleteView(LoginRequiredMixin,DeleteView):
    model=Notes
    success_url= '/smart/notes/' 
    template_name='notes/notes_delete.html'
    login_url='/login'
  
    def get_queryset(self):
      return self.request.user.notes.all()  #only loggedin user will have access to notes
   

            