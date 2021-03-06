from django.shortcuts import render_to_response
from kittehs.models import *

def index(request):
    return render_to_response("index.html", {
        "message": "Hello, world!",
    })
    
def list(request, list_pk):
    l = List.objects.get(pk=list_pk)
    list_name = l.name
    tasks = l.task_set.all()
    dico = {
        "list_name" : list_name,
        "tasks" : tasks,
        }
    return render_to_response("list.html", dico)
    