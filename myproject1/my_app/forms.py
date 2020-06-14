from django import forms
from django.core import validators
from my_app.models import User

class NewUserForm(forms.ModelForm):
    # first_name = User.CharField()
    # last_name = models.CharField()
    # email = models.CharField()
    # verify_email = forms.EmailField('Enter your email once again')
    # bot_catcher = forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
    #
    # def clean(self):
    #     all_clean_data = super().clean()
    #     email = all_clean_data['email']
    #     vmail = all_clean_data['verify_email']
    #
    #     if email != vmail:
    #         raise forms.ValidationError("THE EMAIL NEEDS TO MATCH!")

    class Meta:
        model = User
        fields = '__all__'