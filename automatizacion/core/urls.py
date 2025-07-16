from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
        
    path('maquinaria/', views.vista_maquinaria, name='maquinaria'),

    # URL para la sección de Tesorería
    path('tesoreria/', views.vista_tesoreria, name='tesoreria'),
    
    path('crear_maquinaria/', views.vista_crear_maquinaria, name='crear_maquinaria'),
    
    path('maquinaria/detalle/<uuid:id>/', views.ver_detalle_maquina, name='ver_detalle_maquina'),
    
    path('maquinaria/comparar/<uuid:id>/', views.comparar_maquina, name='comparar_maquina'),
    
    path('maquinaria/editar/<uuid:id>/', views.editar_maquina, name='editar_maquina'),
    
    path('api/maquinas/tipo/<str:tipo>/', views.api_maquinas_por_tipo, name='api_maquinas_por_tipo'),
    path('api/maquina/<uuid:id>/', views.api_maquina_detalle, name='api_maquina_detalle'),
    path('api/comparar/<uuid:id1>/<uuid:id2>/', views.api_comparar_maquinas, name='api_comparar_maquinas'),
    
    # URLs de Clientes
    path('clientes/', views.clientes_list, name='clientes_list'),
    path('clientes/crear/', views.clientes_crear, name='clientes_crear'),
    path('clientes/editar/<str:pk>/', views.clientes_editar, name='clientes_editar'),
    path('clientes/eliminar/<str:pk>/', views.clientes_eliminar, name='clientes_eliminar'),
    
    # URLs de Proveedores
    path('proveedores/', views.proveedores_list, name='proveedores_list'),
    path('proveedores/crear/', views.proveedores_crear, name='proveedores_crear'),
    path('proveedores/editar/<str:pk>/', views.proveedores_editar, name='proveedores_editar'),
    path('proveedores/eliminar/<str:pk>/', views.proveedores_eliminar, name='proveedores_eliminar'),
    
    # URLs de Registros
    path('registros/', views.registros_list, name='registros_list'),
    path('registros/crear/', views.registros_crear, name='registros_crear'),
    # urls.py
    path('registros/<str:id>/editar/', views.editar_registro, name='registros_editar'),

    path('registros/validar-id/', views.validar_id_registro, name='validar_id_registro'),
    path('clientes/<int:cliente_id>/terminos/', views.obtener_terminos_cliente, name='obtener_terminos_cliente'),
    path('proveedores/<int:proveedor_id>/terminos/', views.obtener_terminos_proveedor, name='obtener_terminos_proveedor'),
    
    path('registros/<str:registro_id>/flujo/', views.flujo_caja_view, name='flujo_caja'),
    path('calcular-flujo/', views.calcular_flujo_caja, name='calcular_flujo'),
    path('dashboard-datos/<int:registro_id>/', views.obtener_datos_dashboard, name='dashboard_datos'),
    path('exportar-reporte/<int:registro_id>/', views.exportar_reporte_flujo, name='exportar_reporte'),
    
    path('registro/importar/', views.cargar_excel_completo, name='cargar_excel_completo'),
    
]