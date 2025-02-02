from django.urls import path
from . import views
urlpatterns = [
    path('', views.index ),
    path('cambio/', views.cambio ),
    path('contacto/', views.contacto ),
    path('about/', views.about ),
    path('news/', views.news ),
    path('new/edit/<int:id>', views.edit_news ),
    path('new/<int:id>', views.new ),
    path('santisimacruz/', views.santisimacruz ),
    path('santisimatrinidad/', views.santisimatrinidad ),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('mensajes/', views.mensajes),
    path('mensajes/eliminar/<int:id>', views.eliminar_mensaje),
]