from django.shortcuts import render
from .models import Places, Person
# Create your views here.
def index(request):
    places = Places.objects.all()
    persons = Person.objects.all()

    print("places xx:", places[0])

    place_person_dict = {}
    for place in places:
        for person in persons:
            if person.place == place:
                if not place.name in place_person_dict:
                    place_person_dict[place.name] = []
                place_person_dict[place.name].append(person.name)
                # print("Person-Place", person, place)
    # print("place_person_dict:", place_person_dict)

    # { "balaghat": ["bhabhi"], "bhopal": ["vivek", "araddhya"]}


    # # return HttpResponse ("Bellllooo from view.py")
    # place1 = Places()
    # place1.num = '1'
    # place1.name = 'Malanjkhand'
    # place1.img = 'malanjkhand.jpg'
    # place1.with_whom = 'Family'
    # place1.when = '1990'
    #
    # places = [place1, place2, place3]

    return render(request, "index.html", {'places': places, 'persons': persons, 'place_person_dict': place_person_dict} )
