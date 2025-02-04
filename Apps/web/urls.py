from django.urls import path
from . import views
urlpatterns = [
    path('', views.index ),
    path('cambio/', views.cambio ),
    path('contacto/', views.contacto ),
    path('about/', views.about ),
    path('news/', views.news ),
    path('new/edit/<int:id>', views.edit_news ),
    path('new/delete/<int:id>', views.delete_new ),
    path('new/<int:id>', views.new ),
    path('santisimacruz/', views.santisimacruz ),
    path('santisimatrinidad/', views.santisimatrinidad ),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('mensajes/', views.mensajes),
    path('mensajes/eliminar/<int:id>', views.eliminar_mensaje),

    path('personas/', views.PersonaListView.as_view(), name='persona_list'),
    path('personas/nuevo/', views.PersonaCreateView.as_view(), name='persona_create'),
    path('personas/<int:pk>/editar/', views.PersonaUpdateView.as_view(), name='persona_update'),
    path('personas/<int:pk>/eliminar/', views.PersonaDeleteView.as_view(), name='persona_delete'),

    path('solicitar-misa/', views.solicitar_misa, name='solicitar_misa'),
    path('ver-solicitudes/', views.ver_solicitudes, name='ver_solicitudes'),
    path('registro/', views.registro, name='registro')
]