# formularz - metoda POST (redirect)
from django.shortcuts import render, redirect, Http404, get_object_or_404
from week_app.models import Died , Comment
from .forms import DiedForm, CommentForm
from django.utils import timezone
from auth_system_app.models import Week


DIEDS = []


# Create a diet

def diet_create_view(request):
    if request.method == "GET":
        form = DiedForm()                                   # Tworzymy formularz dla metoda GET request
        return render(request,
                      'week_app/create_died.html',
                      {'form': form}
                      )

    if request.method == "POST":
        died = request.POST.get('died')
        if died is not None:
            Died.objects.create(name=died)                  # Tworzenie diety z numerem id
            return redirect(
                'week_app:died_list'
            )                                               # przekierowanie do listy diet

        died_id = request.POST.get('died_id')               # Za pomocą POST pobieramy numer id
        if died_id:
            died = get_object_or_404(Died, id=died_id)      # Otrzymaj diete z id(baza danych) albo 404
            form = DiedForm(request.POST, instance=died)
            if form.is_valid():
                died.create_date = timezone.now()           # Tworzenie daaty utworzenia diety
                form.save()                                 # Zapis fomularza django do bazy danych
                return redirect(
                    'week_app:died_detail',
                    died_id=died_id
                )                                           # Widok szczegółów diety

# Read created diet list
def died_list_view(request):
    return render(                                          # Widok listy diet
        request,                                            # uzywam funcji render
        'week_app/died_list.html',
        {
            'died': Died.objects.all(),

        }
    )


# R (szczegół) z CRUD
def died_detail_view(request, died_id):                      # Widok szczegółów diety
    died = get_object_or_404(Died, id=died_id)               # Otrzymaj diete z id(baza danych) albo 404
    return render(
        request,
        'week_app/died_detail.html',
        {
            'died': died,

        }
    )


# U z CRUD
def died_update_view(request, died_id):                      # Widok edycji diety
    died = get_object_or_404(Died, id=died_id)               # Otrzymaj diete z id(baza danych) albo 404
    if request.method == 'POST':
        new_died = request.POST.get('died')                 # Jeżeli Post to nowa dieta
        if new_died is not None:                            # dodaj nową id i nazwe diety
            died.name = new_died
            died.modify_date = timezone.now()               # utwórz date modyfikacji diety
            died.save()                                     # save do database
        form = DiedForm(request.POST, instance=died)        # Tworzę formularz powiązany z modelem diety
        if form.is_valid():
            form.save()

        return redirect(
            'week_app:died_detail',
            died_id=died_id
        )

    else:
        form = DiedForm(instance=died)

    return render(request,
                  'week_app/died_edit.html',

                  {
                      'died': died,
                      'form': form
                  }
                  )
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

    #Dodawanie dity na widoku szczegołów diety za pomocą przycisku dodaj w html

def died_add_view(request, died_id):
    died = get_object_or_404(Died, id=died_id)

    if request.method == 'POST':
        form = DiedForm(request.POST, instance=died)
        if form.is_valid():
            died.create_date = timezone.now()
            form.save()
            return redirect('week_app:died_detail', died_id=died_id)

    else:
        form = DiedForm(instance=died)

    return render(request,
                  'week_app/died_add.html',
                  {
                      'died': died,
                      'form': form
                  }
                  )
# Comments add view
def comment_add_view(request, died_id):
    died = get_object_or_404(Died, id=died_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.died = died
            comment.save()
            return redirect('week_app:died_detail', died_id=died_id)
    else:
        form = CommentForm()

    return render(request, 'week_app/comment_add.html', {'died': died, 'form': form})





