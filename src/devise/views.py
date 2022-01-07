from django.shortcuts import render, redirect
# Create your views here.
import api


def redirect_home(request):
    return redirect("home", days_range=30, currencies="CAD")


def dashboard(request, days_range=20, currencies="USD"):
    # Comme on ne peut pas passer de liste à l'URL on envoie une chaine de carractère avec tous les currencies
    # "USD, EUR, CHF" sous forme d'une chaine de caractère séparé d'une virgule

    days, rates = api.get_rates(currencies=currencies.split(','), days=days_range)
    page_label = { 7: "Semaine", 30: "Mois", 365: "Année"}.get(days_range, "Personnalité")
    return render(request, "devise/index.html", context={"data": rates,
                                                         "days_labels": days,
                                                         'currencies': currencies,
                                                         "page_label": page_label})

