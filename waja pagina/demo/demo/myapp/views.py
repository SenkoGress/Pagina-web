from django.shortcuts import render, HttpResponse, redirect
from .forms import RegistrarUsuarioForm, IniciarSesionForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def waja(request):
    data={'popim':'34'}
    return render(request, "waja.html",data)

def lolein(request):
    data={'registro':RegistrarUsuarioForm}
    #data[(nombrepagina:variable)]
    


# if request.user.is_authenticated and not (request.user.is_staff):
#         return redirect(index2)
#     if request.user.is_authenticated and request.user.is_staff:
#         return redirect(adminPage)

    # data = {"form": RegistrarUsuarioForm, "mesg" : ""}
    if request.method == "POST":
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                # rutUsuario = request.POST.get("rutUsuario")
                # direccion = request.POST.get("direccion")
                # esSuscriptor = request.POST.get("esSuscriptor")
                # if esSuscriptor == 'on':
                #     esSuscriptor = True
                # elif esSuscriptor == None:
                #     esSuscriptor = False
                # imagen = request.FILES.get("imagen")
                #imagen = request.FILES.get("imagen")
                #PerfilUsuario.objects.update_or_create(user = user, rutUsuario = rutUsuario, direccion = direccion,esSuscriptor = esSuscriptor, imagen=imagen)
                data["mesg"] = "La cuenta ha sido creada"
            except Exception as e:
                print(e)
                data["mesg"] = "La cuenta no ha sido creada"

        else: 
            data["mesg"] = "Revise sus datos de ingreso"
    return render(request, "lolein.html",data)

def contacto(request):
    return render(request, "contacto.html")

def loginmalo(request):
    return render(request, "login.html")


def cerrarSesion(request):
    logout(request)
    return redirect(waja)

    
def log(request):
    if request.user.is_authenticated and not (request.user.is_staff):
        return redirect(waja)
    data = {"form": IniciarSesionForm, "mesg":""}
    if request.method == "POST": 
        form = IniciarSesionForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(waja)
                else:
                    data["mesg"] = "¡La cuenta o la password no son correctos!"
            else:
                data["mesg"] = "¡La cuenta o la password no son correctos!"
    return render(request, "log.html",data)

def Especias1(request):
    return render(request, "Especias1.html")

def Especias2(request):
    return render(request, "Especias2.html")

def Especias3(request):
    return render(request, "Especias3.html")

def Especias4(request):
    return render(request, "Especias4.html")

def Especias5(request):
    return render(request, "Especias5.html")

def Especias6(request):
    return render(request, "Especias6.html")

def Especias7(request):
    return render(request, "Especias7.html")

def Especias8(request):
    return render(request, "Especias8.html")

def Especias9(request):
    return render(request, "Especias9.html")

def Especias10(request):
    return render(request, "Especias10.html")

def Especias11(request):
    return render(request, "Especias11.html")

def Especias12(request):
    return render(request, "Especias12.html")

def Carrito(request):
    return render(request, "Carrito.html")