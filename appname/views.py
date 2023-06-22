from django.shortcuts import render, redirect
from appname.models import Restaurant
from django.http import HttpResponseRedirect
from django.urls import reverse
import json

def search_form_view(request):
    if request.method == 'POST':
        query = request.POST.get('query')  # Assuming the search input field name is 'query'
        #return HttpResponseRedirect(reverse('appname:results') + f'?query={query}')
        return redirect('results', query=query)

    return render(request, 'search_form.html')


def results_view(request, query):
    results = []
    restaurants = Restaurant.objects.all()
    for restaurant in restaurants:
        items = json.loads(restaurant.items)
        if query.lower() in map(str.lower, items.keys()):
            results.append(restaurant)
    
    return render(request, 'results.html', {'results': results, 'query': query})


