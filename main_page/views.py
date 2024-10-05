from django.shortcuts import render, redirect
from .models import todo  # Лучше использовать стандартный стиль наименований моделей

# Создаем задачу
def home(request):
    if request.method == "POST":
        desc = request.POST.get("desc")# Убираем лишние пробелы

        if desc:  # Проверяем, что описание не пустое
            todo.objects.create(description=desc)
        return redirect("home")

    return render(request, 'index.html')


# Получаем список всех задач
def get_datas(request):
    datas = todo.objects.all()
    return render(request, 'to_do_lists.html', {"data": datas})
