from django import forms
from .models import StickyNote

# Form for creating and updating StickyNote instances
class StickyNoteForm(forms.ModelForm):
    class Meta:
        # Specify the model for the form
        model = StickyNote
        # Specify the fields to include in the form
        fields = ['title', 'content', 'color']