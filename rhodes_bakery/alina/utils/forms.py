from django import forms
from alina.models import Login
from alina.utils.over_password import md5
from django.core.exceptions import ValidationError


class Inits:
    exclude_lists = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name in self.exclude_lists:
                continue
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": field.label
                }


class InitModelForm(Inits, forms.ModelForm):
    pass


class LoginMForm(InitModelForm):
    confirm_password = forms.CharField(
        label="再次输入密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = Login
        fields = ["username", "password", "confirm_password"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        print(pwd)
        m_pwd = md5(pwd)
        return m_pwd

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        con_pwd = md5(self.cleaned_data.get("confirm_password"))
        if pwd != con_pwd:
            raise ValidationError("密码不一致")
        return con_pwd
