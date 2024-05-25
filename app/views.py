from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

app_settings_func = {
    "january": "Eat no meat for the entire month!",
    "febuary": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None
}

# Create your views here.


def index(request):
    months = list(app_settings_func.keys())

    return render(request, "app/index.html", {
        "months": months
    })


def app_settings_with_number(request, app):
    application_month = list(app_settings_func.keys())

    if app > len(application_month):
        return HttpResponseNotFound("<h2>Invalid month</h2>")

    redirect_app = application_month[app - 1]
    redirect_path = reverse("app_challenge", args=[redirect_app])
    return HttpResponseRedirect(redirect_path)


def app_settings(request, app):
    try:
        challenge_text = app_settings_func[app]
        return render(request, "app/app.html", {
            "text": challenge_text,
            "month": app.capitalize()
        })
    except:
        return HttpResponseNotFound("<h2>This webpage is not found!</h2>")
