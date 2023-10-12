from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Rating, Recipe
from .forms import RecipeForm, LoginForm, RatingForm, createUserForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def RecipeList(request):
    user = request.user
    if user.id:
        queryset = Recipe.objects.filter(user=user)
        query_rating = Rating.objects.all()
        form = RecipeForm()

        context = {
            "recipes": queryset,
            "user": user,
            "form": form,
            "ratings": query_rating,
        }
        template_name = "api/recipe_list.html"
        if request.method == "POST" and "btn1" in request.POST:
            form = RecipeForm(request.POST, request.FILES)

            if form.is_valid():
                newuser = form.save(commit=False)
                newuser.user_id = request.user.id
                newuser.save()
                form.save()
                form2 = Rating.objects.create(recipe_id=newuser.id)
                form2.save()

                return redirect("/")

    else:
        return redirect("login/")
    return render(request, template_name, context)


def RecipeEdit(request, recipe_id):
    object_name = Recipe.objects.get(id=recipe_id)
    rating_object = Rating.objects.get(recipe_id=recipe_id)
    form = RecipeForm(instance=object_name)
    form2 = RatingForm(instance=rating_object)
    template_name = "api/recipe_edit.html"
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILE, instance=object_name)

        if form.is_valid():
            form.save()
            return redirect("/")

    return render(
        request,
        "api/recipe_edit.html",
        {"form": form, "recipe": object_name, "form2": form2},
    )


def RecipeDelete(request, recipe_id):
    object_name = Recipe.objects.get(id=recipe_id)
    object_name.delete()
    return redirect("/")


def LoginView(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("/")
            else:
                return render(
                    request,
                    "api/login.html",
                    {"massege": "the user NOT found , register here ", "form": form},
                )

    return render(request, "api/login.html", {"form": form})


def registerView(request):
    form = createUserForm()
    if request.method == "POST":
        form = createUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    return render(request, "api/register.html", {"form": form})


def LogoutView(request):
    logout(request)
    return redirect("/login/")


def RateView(request, recipe_id):
    if request.method == "POST":
        id = request.POST.get("id")
        val = request.POST.get("val")
        obj = Rating.objects.get(recipe_id=id)
        obj.stars = val
        obj.save()

    return render(request, "api/rating.html", {"recipe": recipe_id})
