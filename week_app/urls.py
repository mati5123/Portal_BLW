from django.urls import path

from week_app import views

app_name = 'week_app'

urlpatterns = [
    # C z CRUD
    path('died/create/', views.diet_create_view, name='create_died'),
    # R z CRUD (lista)
    path('died/', views.died_list_view, name='died_list'),

    # R z CRUD (szczegół)
    path('died/<int:died_id>/', views.died_detail_view, name='died_detail'),
    # U z CRUD
    path('died/<int:died_id>/edit/', views.died_update_view, name='died_update'),
    # D z CRUD
    path('died/<int:died_id>/delete/', views.died_delete_view, name='died_delete'),
    # C z CRUD
    #path('died/<int:died_id>/died_add/', views.died_add, name='create_died_text'),

]
