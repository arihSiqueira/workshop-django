from django import forms

class QuestionForm(forms.Form):
    question = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Sua pergunta"
        })
    )