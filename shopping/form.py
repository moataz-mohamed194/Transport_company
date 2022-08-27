from django import forms


class SearchForm(forms.Form):
    number = forms.CharField(
        required=False,
        label="رقم العربة",
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   'maxlength': '100',
                   "autocomplete": "off",
                   "placeholder": "رقم العربة",
                   "style": "text-align: end;"}
        ),
    )

    load = forms.CharField(
        required=False,
        label="الحمولة",
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "autocomplete": "off",
                   "placeholder": "الحمولة",
                   "style": "text-align: end;"}
        ),
    )
    get_in = forms.DateField(
        required=False,
        label="تاريخ الدخول",
        widget=forms.DateInput(
            attrs={"class": "form-control",
                   "type": "date",
                   "autocomplete": "off",
                   "placeholder": "تاريخ الدخول",
                   "style": "text-align: end;color: #6c757d;"}
        ),
        input_formats=["%m-%d-%Y", "%Y-%m-%d"],
    )

    get_out = forms.DateField(
        required=False,
        label="تاريخ الخروج",
        widget=forms.DateInput(
            attrs={"class": "form-control",
                   "type": "date",
                   "autocomplete": "off",
                   "placeholder": "تاريخ الخروج",
                   "style": "text-align: end;color: #6c757d;"}
        ),
        input_formats=["%m-%d-%Y", "%Y-%m-%d"],
    )
    driver_name = forms.CharField(
        required=False,
        label="اسم السائق",
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "autocomplete": "off",
                   "placeholder": "اسم السائق",
                   "style": "text-align: end;"}
        ),
    )


class AddForm(forms.Form):
    number = forms.CharField(
        required=True,
        label="رقم العربة",
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "autocomplete": "off",
                   "placeholder": "رقم العربة",
                   "style": "text-align: end;"}
            ),
    )
    load = forms.CharField(
        required=True,
        label="الحمولة",
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "autocomplete": "off",
                   "placeholder": "الحمولة",
                   "style": "text-align: end;"}
        ),
    )
    get_in = forms.DateField(
        required=True,
        label="تاريخ الدخول",
        widget=forms.DateInput(
            attrs={"class": "form-control",
                   "type": "date",
                   "autocomplete": "off",
                   "placeholder": "تاريخ الدخول",
                   "style": "text-align: end;color: #6c757d;"}
        ),
        input_formats=["%m-%d-%Y", "%Y-%m-%d"],
    )

    get_out = forms.DateField(
        required=True,
        label="تاريخ الخروج",
        widget=forms.DateInput(
            attrs={"class": "form-control",
                   "type": "date",
                   "autocomplete": "off",
                   "placeholder": "تاريخ الخروج",
                   "style": "text-align: end;color: #6c757d;"}
        ),
        input_formats=["%m-%d-%Y", "%Y-%m-%d"],
    )
    driver_name = forms.CharField(
        required=True,
        label="اسم السائق",
        widget=forms.TextInput(
            attrs={"class": "form-control",
                   "autocomplete": "off",
                   "placeholder": "اسم السائق",
                   "style": "text-align: end;"}
        ),
    )
