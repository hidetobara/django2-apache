from django.http import HttpResponse
from django.shortcuts import render

def detail(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id)

def hello(request):
    if request.method == 'GET':
        context = {
            'message': "Hell world.",
            'items': [
                {'name': 'hoge'},
                {'name': 'fuga'},
            ],
        }
        return render(request, 'hello/index.html', context)