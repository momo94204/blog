from django import forms
from iphone.models import Iphone


class IphoneForm(forms.ModelForm):
    title = forms.CharField(label='產品名稱', max_length=128)
    content = forms.CharField(label='產品內容', widget=forms.Textarea)

    class Meta:
        model = Iphone
        fields = ['title', 'content']