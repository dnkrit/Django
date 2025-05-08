from django import forms
from .models import News_post
import datetime

class NewsForm(forms.ModelForm):
    pub_date_date = forms.DateField(
        label='Дата публикации',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control mb-3'})
    )
    pub_date_time = forms.TimeField(
        label='Время публикации',
        widget=forms.TimeInput(attrs={'type': 'time', 'class': 'form-control mb-3'})
    )

    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'short_description': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'text': forms.Textarea(attrs={'class': 'form-control mb-3'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        date = self.cleaned_data['pub_date_date']
        time = self.cleaned_data['pub_date_time']
        instance.pub_date = datetime.datetime.combine(date, time)
        if commit:
            instance.save()
        return instance
