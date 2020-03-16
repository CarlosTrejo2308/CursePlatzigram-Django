from django.http import HttpResponse
from datetime import datetime
from django.http import JsonResponse
import json

#Returns a greeting
def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')

    return HttpResponse('Oh, hi! Current server time is {now}'.format
        (now=str(now))
    )

#Return a json response with sorted integers
def sorted(request):
    #Debugger
    #import pdb; pdb.set_trace()

    #Getting the numbers by post method (url/?numbers=...)
    numbers = request.GET['numbers']
    # print(numbers)
    # print(type(numbers))

    #Passing to a list
    numbers_list = numbers.split(',')
    # print(numbers_list)
    # print(type(numbers_list))

    #Cobverting to int's
    numbers_list = [int(i) for i in numbers_list]

    #Sorting
    numbers_list.sort()
    # print(numbers_list)

    data = {
        'status': 'ok',
        'numbers': numbers_list,
        'message': 'Integers sorted successfully'
    }

    #Passing to JsonResponse
    #response = JsonResponse({'numbers': numbers_list})
    hresponse = HttpResponse(json.dumps(data, indent=4),
        content_type = 'application/json'
    )

    jresponse = JsonResponse(numbers_list, safe=False)

    return hresponse

#Checks if the age fullfills the legal requirement
#and returns if the user is allowed or not to enter the page
def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello {}, welcome to platzigram'.format(name)

    return HttpResponse(message)
