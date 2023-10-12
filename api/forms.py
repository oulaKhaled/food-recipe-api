from django.forms import (
    ModelForm,
    TextInput,
    NumberInput,
    TimeInput,
    FileInput,
    Textarea,
    EmailInput,
    PasswordInput,
)
from .models import Rating, Recipe
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["name", "description", "ingredients", "time", "image"]
        exclude = ["user_id"]

        widgets = {
            "name": TextInput(
                attrs={
                    "placeholder": "recipe name",
                    "style": "width: 300px; ",
                    "class": "form-control",
                }
            ),
            "ingredients": TextInput(
                attrs={
                    "placeholder": "ingredients",
                    "style": "width: 300px;",
                    "class": "form-control",
                }
            ),
            "time": NumberInput(
                attrs={
                    "placeholder": "time",
                    "style": "width: 300px; ",
                    "class": "form-control",
                }
            ),
            "image": FileInput(
                attrs={
                    "placeholder": "recipe image",
                    "style": "width: 300px;",
                    "class": "form-control",
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "recipe description",
                    "style": "width: 500px;",
                    "class": "form-control",
                }
            ),
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=70,
        widget=forms.TextInput(
            attrs={
                "placeholder": "username",
                "style": "width: 300px;",
                "class": "form-control",
            }
        ),
    )
    password = forms.CharField(
        max_length=65,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "username",
                "style": "width: 300px;",
                "class": "form-control",
            }
        ),
    )

    class Meta:
        fields = ["username", "password"]


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ["stars"]
        exclude = ["recipe"]
        widgets = {
            "stars": NumberInput(
                attrs={
                    "placeholder": "stars",
                    "style": "width: 300px; border-radius: 50px;",
                    "class": "form-control",
                }
            )
        }


class createUserForm(UserCreationForm):
    username = forms.CharField(
        label="username",
        min_length=5,
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "placeholder": "username",
                "style": "width: 300px; align-items: center;",
                "class": "form-control",
            }
        ),
    )
    email = forms.EmailField(
        label="email",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "style": "width: 300px; align-items: center;",
                "class": "form-control",
            }
        ),
    )
    password1 = forms.CharField(
        label="password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "pssword",
                "style": "width: 300px; align-items: center;",
                "class": "form-control",
            }
        ),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "pssword",
                "style": "width: 300px; align-items: center;",
                "class": "form-control",
            }
        ),
    )
