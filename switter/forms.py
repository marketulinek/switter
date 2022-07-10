from django import forms
from .models import Sweet


class SweetForm(forms.ModelForm):
    content = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                'placeholder': 'Ssss something...',
                'class': 'textarea is-medium is-snake',
                'rows': 5
            }
        ),
        label = ''
    )

    class Meta:
        model = Sweet
        exclude = ('user', )