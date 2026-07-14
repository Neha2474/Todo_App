from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import todoData
# Create your views here.

def todos(request):
    #return HttpResponse("Hello World")
    td = todoData.objects.all()

    if request.method == "POST":

        if "add_task" in request.POST:
            title = request.POST.get("title")
            if title:
                todoData.objects.create(title=title)
            return redirect("todos")

        if "edit_task" in request.POST:
            task_id = request.POST.get("task_id")
            new_title = request.POST.get("new_title")
            td = get_object_or_404(todoData,id=task_id)
            td.title = new_title
            td.save()
            return redirect("todos")

        if "clear_task" in request.POST:
            todoData.objects.all().delete()
            return redirect("todos")

        if "delete_task" in request.POST:
            task_id = request.POST.get("task_id")
            td = get_object_or_404(todoData,id=task_id)
            td.delete()
            return redirect("todos")


    template = loader.get_template('todopage.html')
    context = {'td':td, 'count':td.count()}
    return HttpResponse(template.render(context,request))
