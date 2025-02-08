from django.urls import path
from . import views
urlpatterns = [
    path('', views.index ),
    path('cambio/', views.cambio ),
    path('contacto/', views.contacto ),
    path('about/', views.about ),
    path('liturgia/', views.liturgia ),
    path('horarios/', views.horarios ),
    path('calendarios/', views.calendarios ),
    path('sacramentos/', views.sacramentos ),
    path('oracion/', views.oracion ),
    path('galeria/', views.galeria ),
    path('padre/', views.padre ),
    path('vicario/', views.vicario ),
    path('monsenor/', views.monsenor ),
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
    
    path('aprobar_solicitud_misa/<int:reserva_id>/', views.aprobar_solicitud_misa, name='aprobar_solicitud_misa'),
    path('rechazar_solicitud_misa/<int:reserva_id>/', views.rechazar_solicitud_misa, name='rechazar_solicitud_misa'),
    
    path('registro/', views.registro, name='registro'),
    
    path('solicitar-bautizo/', views.solicitar_bautizo, name='solicitar_bautizo'),
    path('ver-solicitudes-bautizos/', views.ver_solicitudes_bautizos, name='ver_solicitudes_bautizos'),
     path('aprobar_solicitud_bautizo/<int:bautizo_id>/', views.aprobar_solicitud_bautizo, name='aprobar_solicitud_bautizo'),
    path('rechazar_solicitud_bautizo/<int:bautizo_id>/', views.rechazar_solicitud_bautizo, name='rechazar_solicitud_bautizo'),
    
    path('solicitar-matrimonio/', views.solicitar_matrimonio, name='solicitar_matrimonio'),
    path('ver-solicitudes-matrimonios/', views.ver_solicitudes_matrimonios, name='ver_solicitudes_matrimonios'),
    path('aprobar_solicitud_matrimonio/<int:matrimonio_id>/', views.aprobar_solicitud_matrimonio, name='aprobar_solicitud_matrimonio'),
    path('rechazar_solicitud_matrimonio/<int:matrimonio_id>/', views.rechazar_solicitud_matrimonio, name='rechazar_solicitud_matrimonio'),
]