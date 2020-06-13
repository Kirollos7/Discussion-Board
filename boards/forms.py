from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows':5,'placeholder':'What is in your mind?'}
    ),max_length=10000 , help_text='The Max Length of the text is 5000')

    class Meta:
        model = Topic
        fields = ['subject', 'message']


