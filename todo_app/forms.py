from django import forms


class ToDoForm(forms.Form):
    text = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Enter todo ",
    }))
