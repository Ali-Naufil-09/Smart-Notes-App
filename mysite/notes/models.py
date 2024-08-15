from django.db import models

#importing user so that  any user can create,edit,delete notes
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    title=models.CharField(max_length=200)
    text=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    #these are the outsiders(users) who will use our app
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='notes') #if the user want to delete its account then we will have to delete all the data associated to the user
    