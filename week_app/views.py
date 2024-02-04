# formularz - metoda POST (redirect)
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from week_app.models import Died, Comment
from .forms import DiedForm, CommentForm, ImageForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required


DIEDS = []


# Create a diet
@login_required
def died_create_view(request, week_nr, ):
    if request.method == "GET":
        form = DiedForm()
        return render(
            request,
            'week_app/create_died.html',
            context={
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
            )  # przekierowanie do listy diet
        else:
            return HttpResponse("Niepoprawne dane")


def died_list_view(request, week_nr):
    return render(  # Widok listy diet
        request,  # uzywam funcji render
        'week_app/died_list.html',
        {
            'died': Died.objects.filter(week_number=week_nr),
            'week_nr': week_nr,

        }
    )


# R (szczegół) z CRUD
def died_detail_view(request, died_id):  # Widok szczegółów diety
    died = get_object_or_404(Died, id=died_id)  # Otrzymaj diete z id(baza danych) albo 404
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

@login_required
def died_update_view(request, died_id):  # Widok edycji diety
    died = get_object_or_404(Died, id=died_id)  # Otrzymaj diete z id(baza danych) albo 404
    if request.method == 'POST':
        new_died = request.POST.get('died')  # Jeżeli Post to nowa dieta
        if new_died is not None:  # dodaj nową id i nazwe diety
            died.name = new_died
            died.modify_date = timezone.now()  # utwórz date modyfikacji diety
            died.save()  # save do database

        # image = request.FILES['image']
        image = request.FILES.get('image')
        if image is not None:
            died.image = image
            died.save()

        form = DiedForm(request.POST, instance=died)  # Tworzę formularz powiązany z modelem diety celem edycji tekstu
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
@login_required
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

        return redirect(
            'week_app:died_list',
            week_nr=week_nr
        )


""""------------------------------------- Comments----------------------------"""
@login_required
def comment_add_view(request, died_id):
    died = get_object_or_404(Died, id=died_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.died = died
            comment.created_date = timezone.now()
            comment.user = request.user  # Zapisz do bazy kto jest autorem komentarza
            comment.save()
            return redirect('week_app:died_detail',
                            died_id=died_id)

    else:
        form = CommentForm()

    return render(request,
                  'week_app/comment_add.html',
                  {
                      'died': died,
                      'form': form}
                  )

@login_required
def comment_delete_view(request, died_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Sprawdz czy autor komentarza jest zalogowany.
    if request.user != comment.user:
        return render(request, 'week_app/not_author.html',
                      {
                          'comment': comment,
                          'died_id': died_id
                      }
                      )

    if request.method == 'POST':
        comment.delete()
        return redirect(
            'week_app:died_list',
            week_nr=comment.died.week_number)
    else:
        return render(
            request,
            'week_app/comment_confirm_delete.html',
            {
                'comment': comment,
                'died_id': died_id
            }
        )

"""---------------------------------Image------------------------------"""


@login_required
def create_image_view(request, died_id):
    died = get_object_or_404(Died, id=died_id)

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            images = form.save(commit=False)
            images.died = died
            images.save()

            return redirect(
                'week_app:died_detail',
                died_id=died_id
            )  # Przekierowanie do porzedniej strony z dietą
    else:
        form = ImageForm()

    return render(request,
                  'week_app/image_add.html',
                  {
                      'died': died,
                      'form': form,
                  }
                  )
