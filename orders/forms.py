from django import forms

from .models import Order


class ContactForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 4:
            raise forms.ValidationError(
                "Имя должно состоять не менее чем из 3 символов")
        return name

    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) < 10:
            raise forms.ValidationError(
                "Подробнее опишите необходимый товар")
        return message

    class Meta:
        model = Order
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ваше имя...'}),
            'email': forms.TextInput(
                attrs={'placeholder': 'Email для связи...'}),
            'message': forms.Textarea(attrs={'cols': 40, 'rows': 3,
                                             'placeholder': 'Ваше сообщение...'})

        }
