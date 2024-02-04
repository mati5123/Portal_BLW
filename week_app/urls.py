from django.urls import path
from week_app import views

app_name = 'week_app'

urlpatterns = [
    # C z CRUD
    path('died/create/<int:week_nr>/', views.died_create_view, name='create_died'),
    # R z CRUD (lista)
    path('died/<int:week_nr>', views.died_list_view, name='died_list'),

    # R z CRUD (szczegół)
    path('died/<int:died_id>/', views.died_detail_view, name='died_detail'),
    # U z CRUD  (edytuj)
    path('died/<int:died_id>/edit/', views.died_update_view, name='died_update'),
    # D z CRUD
    path('died/<int:week_nr>/<int:died_id>/delete/', views.died_delete_view, name='died_delete'),
    # C z CRUD
    path('died/<int:died_id>/add-comment/', views.comment_add_view, name='died_comment_add'),
    # D z CRUD
    path('died/<int:died_id>/comment/<int:comment_id>/delete/', views.comment_delete_view, name='died_comment_delete'),
    # C z CRUD
    path('died/<int:died_id>/image/', views.create_image_view, name='create_image'),



]
