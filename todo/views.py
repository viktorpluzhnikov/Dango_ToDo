from django.shortcuts import render, redirect
from .models import Todo


def index(request):
    todos = Todo.objects.all()
    context = {"todos": todos}
    if request.method == 'POST':
        if "Add" in request.POST:
            task_name = request.POST["task_name"]  # сам текст
            task_date = str(request.POST["task_date"])  # дата, до которой должно быть закончено дело
            #content = task_name + " -- " + task_date + " "  # полный склеенный контент
            todo = Todo(task_name=task_name, task_status=False, task_data=task_date)
            todo.save()  # сохранение нашего дела
            #return redirect("/todos")  # перегрузка страницы (ну вот так у нас будет устроено очищение формы)

        # if "Delete" in request.POST:  # если пользователь собирается удалить одно дело
        #     checkedlist = request.POST.getlist('checkedbox')  # берем список выделенные дел, которые мы собираемся удалить
        #     for i in range(len(checkedlist)):  # мне почему-то не нравится эта конструкция
        #         todo = Todo.objects.filter(id=int(checkedlist[i]))
        #         todo.delete()  # удаление дела
    return render(request, 'main.html', context)


