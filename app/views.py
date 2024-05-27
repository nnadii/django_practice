from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import Month


# Create your views here.


def index(request):
    # all_month = Month.objects.all()
    # for month in all_month:
    #     return HttpResponse("<h2>" + str(month.name) + "</h2>")
    return HttpResponse("Hello world")


# def app_settings_with_number(request, app):
#     all_month = Month.objects.all()

#     for month in all_month:
#         application_month = list(str(month.january))

#         if app > len(application_month):
#             return HttpResponseNotFound("<h2>Invalid month</h2>")

#         redirect_app = application_month[app - 1]
#         redirect_path = reverse("app_challenge", args=[redirect_app])
#         return HttpResponseRedirect(redirect_path)


# def app_settings(request, app):
#     try:
#         challenge_text = app_settings_func[app]
#         return render(request, "app/app.html", {
#             "text": challenge_text,
#             "month": app.capitalize()
#         })
#     except:
#         return HttpResponseNotFound("<h2>This webpage is not found!</h2>")
