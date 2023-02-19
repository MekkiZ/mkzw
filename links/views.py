from django.shortcuts import render


def home_links(request):
    return render(request, 'links/allslinks.html')
