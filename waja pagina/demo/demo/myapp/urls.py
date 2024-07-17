from django.urls import path
from . import views

urlpatterns = [
    path("", views.waja, name="waja"),
    path("waja.html", views.waja, name="waja"),
    path("lolein.html", views.lolein, name="lolein"),
    path("contacto.html", views.contacto, name="conctacto"),
    path("login.html", views.loginmalo, name="login"),
    path("log.html", views.log, name="log"),
    path("Especias1.html", views.Especias1, name="Especias1"),
    path("Especias2.html", views.Especias2, name="Especias2"),
    path("Especias3.html", views.Especias3, name="Especias3"),
    path("Especias4.html", views.Especias4, name="Especias4"),
    path("Especias5.html", views.Especias5, name="Especias5"),
    path("Especias6.html", views.Especias6, name="Especias6"),
    path("Especias7.html", views.Especias7, name="Especias7"),
    path("Especias8.html", views.Especias8, name="Especias8"),
    path("Especias9.html", views.Especias9, name="Especias9"),
    path("Especias10.html", views.Especias10, name="Especias10"),
    path("Especias11.html", views.Especias11, name="Especias11"),
    path("Especias12.html", views.Especias12, name="Especias12"),
    path("Carrito.html", views.Carrito, name="Carrito"),
    path('logout',views.cerrarSesion,name="logout")
]