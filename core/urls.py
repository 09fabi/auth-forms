from django.urls import path
from .views import home, products, exit, admin_home, user_home, CreateActivoView, CreateReportView, ActivosView, ReportsView, eliminar_activo, eliminar_reporte

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('exit/', exit, name='exit'),
    path('admin_home/', admin_home, name='admin_home'),
    path('user_home/', user_home, name='user_home'),
    path('create_activo/', CreateActivoView.as_view(), name='create_activo'),
    path('create_report/', CreateReportView.as_view(), name='create_report'),
    path('activos/', ActivosView.as_view(), name='activos'),
    path('reports/', ReportsView.as_view(), name='reports'),
    path('eliminar_activo/<int:activo_id>/',
         eliminar_activo, name='eliminar_activo'),
    path('eliminar_reporte/<int:report_id>/',
         eliminar_reporte, name='eliminar_reporte'),
]
