# formularz - metoda POST (redirect)
from django.shortcuts import render, redirect, Http404, get_object_or_404, HttpResponse
from week_app.models import Died, Comment, Image
from .forms import DiedForm, CommentForm, ImageForm
from django.utils import timezone

DIEDS = []


# Create a diet
def died_create_view(request, week_nr,):
    if request.method == "GET":
        form = DiedForm()
        return render(
            request,
            'week_app/create_died.html',
            context = {
                'form': form,
                'week_nr': week_nr,

            }
        )

    if request.method == "POST":
        died = request.POST.get('died')
        text = request.POST.get('text')


        if died is not None:
            Died.objects.create(
                name=died,
                text=text,
                week_number=week_nr,
                image=request.FILES.get('image')

            )

            return redirect(
                'week_app:died_list', week_nr=week_nr
            )                                               # przekierowanie do listy diet
        else:
            return HttpResponse("Niepoprawne dane")

        # died_id = request.POST.get('died_id')               # Za pomocą POST pobieramy numer id
        # if died_id:
        #     died = get_object_or_404(Died, id=died_id)      # Otrzymaj diete z id(baza danych) albo 404
        #     form = DiedForm(request.POST, instance=died)
        #     if form.is_valid():
        #         died.create_date = timezone.now()           # Tworzenie daty utworzenia diety
        #         form.save()                                 # Zapis fomularza django do bazy danych
        #         return redirect(
        #             'week_app:died_detail',
        #             died_id=died_id
        #         )                                           # Widok szczegółów diety


def died_list_view(request, week_nr):
    return render(                                                  # Widok listy diet
        request,                                                    # uzywam funcji render
        'week_app/died_list.html',
        {
            'died': Died.objects.filter(week_number=week_nr),
            'week_nr': week_nr,

        }
    )

# R (szczegół) z CRUD
def died_detail_view(request, died_id):                          # Widok szczegółów diety
    died = get_object_or_404(Died, id=died_id)                   # Otrzymaj diete z id(baza danych) albo 404
    # comments = Comment.objects.filter(died=died)
    # image = Image.objects.filter( died_id=died_id)
    return render(
        request,
        'week_app/died_detail.html',
        {
            'died': died,
            # 'comments': comments,
            # 'image': image

        }
    )


# U z CRUD
def died_update_view(request, died_id):                         # Widok edycji diety
    died = get_object_or_404(Died, id=died_id)                  # Otrzymaj diete z id(baza danych) albo 404
    if request.method == 'POST':
        new_died = request.POST.get('died')                     # Jeżeli Post to nowa dieta
        if new_died is not None:                                # dodaj nową id i nazwe diety
            died.name = new_died
            died.modify_date = timezone.now()                   # utwórz date modyfikacji diety
            died.save()  # save do database

        #image = request.FILES['image']
        image = request.FILES.get('image')
        if image is not None:
            died.image = image
            died.save()

        form = DiedForm(request.POST, instance=died)            # Tworzę formularz powiązany z modelem diety celem edycji tekstu
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
                      'form': form,

                  }
                  )


# D z CRUD
def died_delete_view(request, died_id, week_nr):
    died = get_object_or_404(Died, id=died_id)

    if request.method == "GET":
        return render(
            request,
            'week_app/died_confirm_delete.html',
            {
                'died': died,
                'week_nr': week_nr

            }
        )

    elif request.method == "POST":
        data = request.POST
        if 'yes' in data:
            died.delete()

        return redirect('week_app:died_list' ,week_nr=week_nr)


""""------------------------------------- Comments----------------------------"""

def comment_add_view(request, died_id):
    died = get_object_or_404(Died, id=died_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.died = died
            comment.created_date = timezone.now()
            comment.save()
            return redirect('week_app:died_detail', died_id=died_id)

    else:
        form = CommentForm()

    return render(request,
                  'week_app/comment_add.html',
                  {'died': died,
                   'form': form}

                  )
"""---------------------------------Image------------------------------"""
def create_image_view(request, died_id):
    died = get_object_or_404(Died, id=died_id)

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            images = form.save(commit=False)
            images.died = died
            images.save()

            return redirect('week_app:died_detail', died_id=died_id)  # Przekierowanie do porzedniej strony z dietą
    else:
        form = ImageForm()

    return render(request,
                  'week_app/image_add.html',
                  {
                      'died': died,
                      'form': form,
                           }
                  )



