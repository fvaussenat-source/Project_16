from django.shortcuts import render, HttpResponse
# Create your views here.
import api


def dashboard(request, days_range=20, currencies="USD"):
    # Comme on ne peut pas passer de liste à l'URL on envoie une chaine de carractère avec tous les currencies
    # "USD, EUR, CHF" sous forme d'une chaine de caractère séparé d'une virgule

    days, rates = api.get_rates(currencies=currencies.split(','), days=days_range)
    return render(request, "devise/index.html", context={"data": rates["CHF"],
                                                         "days_labels": days})
