from django.shortcuts import render
from .models import Places
# Create your views here.
def index(request):
    places = Places.objects.all()
    # # return HttpResponse ("Bellllooo from view.py")
    # place1 = Places()
    # place1.num = '1'
    # place1.name = 'Malanjkhand'
    # place1.img = 'malanjkhand.jpg'
    # place1.with_whom = 'Family'
    # place1.when = '1990'
    #
    # place2 = Places()
    # place2.num = '2'
    # place2.name = 'Balaghat'
    # place2.img = 'balaghat.jpg'
    # place2.with_whom = 'Family'
    # place2.when = '1993'
    #
    # place3 = Places()
    # place3.num = '3'
    # place3.name = 'Jabalpur'
    # place3.img = 'jabalpur.jpg'
    # place3.with_whom = 'Family'
    # place3.when = '1995'
    #
    # places = [place1, place2, place3]

    return render(request, "index.html", {'places': places} )
