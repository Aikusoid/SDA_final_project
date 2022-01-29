from django import forms


class BootstrapEmailWidget(forms.EmailInput):
    def __init__(self, attrs={}):
        attrs.update({'class': 'form-control'})
        super(BootstrapEmailWidget, self).__init__(attrs=attrs)


class CustomDatetimeInput(forms.DateTimeInput):
    input_type = 'date'


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(max_length=512)
    billing_address = forms.CharField(max_length=512)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, widget=BootstrapEmailWidget)
    datetime_test = forms.DateTimeField(widget=CustomDatetimeInput)

    def clean_username(self):
        return self.cleaned_data['username'].capitalize()

    def __init__(self, min_likes, *args, **kwargs):
        super(CheckoutForm, self).__init__(*args, **kwargs)