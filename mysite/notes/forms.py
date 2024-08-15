from django import forms 
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=('title','text')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control my-3'}), #addding bootstrap form-centrol class to make it nicer
            'text': forms.Textarea(attrs={'class':'form-control my-3'}),
        }
        labels={'text':'Write your thoughts'}  #creting a label of write your thoughts
    
#creating an optionsal condition    
#creating a restriction on title of notes . We will only accept note if title contains naufil word

#def clean_title(self):
#    title=self.cleaned_data['title']
#    if 'naufil' not in title:
#        raise forms.ValidationError('We only accept forms with word naufil in them')
#    return title 
       
    