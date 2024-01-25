# formularz - metoda POST (redirect)
from django.shortcuts import render, redirect, Http404, get_object_or_404

from week_app.models import Died

DIEDS = []


# Create a diet
def diet_create_view(request):
    if request.method == "GET":
        return render(
            request,
            'week_app/create_died.html',
        )

    if request.method == "POST":
        died = request.POST.get('died')
        if died is not None:
            Died.objects.create(name=died)

        return redirect('week_app:died_list')


# Read created diet list
def died_list_view(request):
    return render(
        request,
        'week_app/died_list.html',
        {
            'died': Died.objects.all()
        }
    )

# R (szczegół) z CRUD
def died_detail_view(request, died_id):
    died = get_object_or_404(Died, id=died_id)

    return render(
        request,
        'week_app/died_detail.html',
        {
            'died': died
        }
    )


# U z CRUD
def died_update_view(request, died_id):
    died = get_object_or_404(Died, id=died_id)

    if request.method == "GET":
        return render(
            request,
            'week_app/died_edit.html',
            {
                'died': died
            }
        )

    if request.method == "POST":
        new_died = request.POST.get('died')
        if new_died is not None:
            died.name = new_died
            died.save() # save to database

        return redirect('week_app:died_list')


# D z CRUD
def died_delete_view(request, died_id):
    died = get_object_or_404(Died, id=died_id)

    if request.method == "GET":
        return render(
            request,
            'week_app/died_confirm_delete.html',
            {
                'died': died
            }
        )

    elif request.method == "POST":
        data = request.POST
        if 'yes' in data:
            died.delete()

        return redirect('week_app:died_list')



