from django import forms
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):

    username = forms.CharField(
        required=True,
        label='اسم المستخدم',
        widget=forms.TextInput(
            attrs={"autofocus": True,
                   "class": "form-control",
                   "autocomplete": False
                   }
        ),
    )
    password = forms.CharField(
        required=True,
        label='كلمه السر',
        widget=forms.PasswordInput(
            attrs={"class": "form-control"
                   },
        )
    )


class SignUpForm(forms.Form):
    userName = forms.CharField(label='اسم الدخول',
                               required=True,
                               widget=forms.TextInput(
                                   attrs={"autofocus": True,
                                          "class": "form-control",
                                          "autocomplete": False}
                                   ),
                               )
    password = forms.CharField(label='كلمة السر',
                               required=True,
                               widget=forms.PasswordInput(
                                   attrs={"class": "form-control"}
                                    )
                               )
    repeatPassword = forms.CharField(label='اعد كتابة كلمه السر',
                                     required=True,
                                     widget=forms.PasswordInput(
                                         attrs={"class": "form-control"}
                                        )
                                     )
    first_name = forms.CharField(label='اسم المستخدم',
                                 required=True,
                                 widget=forms.TextInput(
                                       attrs={"autofocus": True,
                                              "class": "form-control",
                                              "autocomplete": False}
                                   ),
                                 )
    is_admin = forms.BooleanField(required=False, label='هل الحساب حساب ادارى ؟')

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        repeat_password = self.cleaned_data.get("repeatPassword")
        if password and repeat_password and password != repeat_password:
            raise ValidationError("Passwords don't match")
        return password
