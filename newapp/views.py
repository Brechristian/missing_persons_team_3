from django.shortcuts import render

# Create your views here.

missing_persons_list = {
    '1': {
        'id': '1',
        "date_missing": "10/30/2009",
        "last_name": "Sharmarice",
        "first_name": "Halima",
        "age_at_missing": "14",
        "city": "Granger",
        "state": "UT",
        "gender": "F",
        "race": "W"
    },

    '2': {
        'id': '2',
        "date_missing": "10/16/2015",
        "last_name": "Martinez",
        "first_name": "Kimberly",
        "age_at_missing": "16",
        "city": "West Valley City",
        "state": "UT",
        "gender": "F",
        "race": "M"
    },

    '3': {
        'id': '3',
        "date_missing": "07/23/2004",
        "last_name": "Gomez",
        "first_name": "Brenda",
        "age_at_missing": "3",
        "city": "Logan",
        "state": "UT",
        "gender": "F",
        "race": "H"
    },

    '4': {
        'id': '4',
        "date_missing": "05/25/2003",
        "last_name": "Bishop",
        "first_name": "Acacia",
        "age_at_missing": "1",
        "city": "Salt Lake City",
        "state": "UT",
        "gender": "F",
        "race": "W"
    },

    '5': {
        'id': '5',
        "date_missing": "08/03/2020",
        "last_name": "Salazar",
        "first_name": "Maria",
        "age_at_missing": "14",
        "city": "Snowville",
        "state": "UT",
        "gender": "F",
        "race": "H"
    },

    '6': {
        'id': '6',
        "date_missing": "04/09/2020",
        "last_name": "Hernandez-Soto",
        "first_name": "Peggy",
        "age_at_missing": "6",
        "city": "Ogden",
        "state": "UT",
        "gender": "F",
        "race": "H"
    },

    '7': {
        'id': '7',
        "date_missing": "06/24/2021",
        "last_name": "Jimenez",
        "first_name": "Lucero",
        "age_at_missing": "14",
        "city": "West Valley City",
        "state": "UT",
        "gender": "F",
        "race": "H"
    },

    '8': {
        'id': '8',
        "date_missing": "11/08/2013",
        "last_name": "Colindres-Avila",
        "first_name": "Yuris",
        "age_at_missing": "17",
        "city": "West Valley City",
        "state": "UT",
        "gender": "F",
        "race": "M"
    },

    '9': {
        'id': '9',
        "date_missing": "07/15/2021",
        "last_name": "Harris",
        "first_name": "Kandis",
        "age_at_missing": "16",
        "city": "Salt Lake City",
        "state": "UT",
        "gender": "F",
        "race": "W"
    },

    '10': {
        'id': '10',
        "date_missing": "07/30/2006",
        "last_name": "Seal",
        "first_name": "Jaydan",
        "age_at_missing": "1",
        "city": "Garleys Wash",
        "state": "UT",
        "gender": "M",
        "race": "W"
    },

    '11': {
        'id': '11',
        "date_missing": "06/13/2018",
        "last_name": "Lizarraga",
        "first_name": "Jose",
        "age_at_missing": "13",
        "city": "West Valley City",
        "state": "UT",
        "gender": "M",
        "race": "H"
    },

    '12': {
        'id': '12',
        "date_missing": "04/23/2020",
        "last_name": "Cortez Trujillo",
        "first_name": "Eztli",
        "age_at_missing": "21",
        "city": "North Ogden",
        "state": "UT",
        "gender": "M",
        "race": "H"
    },

    '13': {
        'id': '13',
        "date_missing": "10/25/2017",
        "last_name": "Fowles",
        "first_name": "Juan",
        "age_at_missing": "15",
        "city": "Lehi",
        "state": "UT",
        "gender": "M",
        "race": "M"
    },

    '14': {
        'id': '14',
        "date_missing": "08/20/2012",
        "last_name": "Garcia",
        "first_name": "Isai",
        "age_at_missing": "17",
        "city": "West Valley City",
        "state": "UT",
        "gender": "M",
        "race": "M"
    },

    '15': {
        'id': '15',
        "date_missing": "09/01/2015",
        "last_name": "Smith",
        "first_name": "Macin",
        "age_at_missing": "17",
        "city": "St. George",
        "state": "UT",
        "gender": "M",
        "race": "W"
    },

    '16': {
        'id': '16',
        "date_missing": "01/26/2006",
        "last_name": "Sisco-Ramirez",
        "first_name": "Jose",
        "age_at_missing": "4",
        "city": "West Valley City",
        "state": "UT",
        "gender": "M",
        "race": "M"
    }
}


def indexPageView(request):
    context = {
        "missings_persons": missing_persons_list.values
    }
    return render(request, 'newapp/index.html', context)


def aboutPageView(request):
    return render(request, "newapp/about.html")


def missing_personsPageView(request, missing_persons_id):
    # find a missing person from the missing persons id
    missing_persons = missing_persons_list[missing_persons_id]

    # create a context dictionary
    context = {
        "missing_persons": missing_persons
    }

    # render out html template
    return render(request, "newapp/missing_persons.html", context)
