from django import forms
from .models import Movie
from .models import Category
from .models import Review


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'poster', 'description', 'release_date', 'actors', 'category', 'trailer_link']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Optional: Add Bootstrap CSS classes to form fields for styling
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
class MovieSearchForm(forms.Form):
    query = forms.CharField(label='Search Movies', required=False)
    category = forms.ChoiceField(choices=Category.objects.values_list('name', 'name'), required=False, label='Category')

class ReviewForm(forms.ModelForm):
     class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),  # Customize textarea appearance if needed
        }