fafrom pydoc import Doc
from django.shortcuts import render
import datetime
from datetime import date
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Familiar1, Familiar2, Familiar3, FechaConsulta
    
    
def vista_familiares(request):
    info1 = Familiar1(nombre = "Carlos Alberto García", edad = 70, nacimiento = 1951)
    info1.save()
    texto1= f"El primer familiar es {info1.nombre}, su edad es de {info1.edad} años y nacio en {info1.nacimiento}"
    
    info2 = Familiar2(nombre = "Luis Alberto Spinetta", edad = 62, nacimiento = 1950)
    info2.save()
    texto2= f"El segundo familiar es {info2.nombre}, su edad cuando fallecio era {info2.edad} años y nacio en {info2.nacimiento}"

    info3 = Familiar3(nombre = "Ástor Pantaleón Piazzolla", edad = 71, nacimiento = 1921)
    info3.save()
    texto3= f"El tercer familiar es {info3.nombre}, su edad cuando fallecio era {info3.edad} años y nacio en {info3.nacimiento}"
    
    fecha_consulta = FechaConsulta(fecha = date.today())
    fecha_consulta.save()
    texto4 = f"La fecha actual de la consulta es: {fecha_consulta.fecha}"
        
    
    return render(request, "template.html", {"texto1" : texto1,"texto2" : texto2, "texto3" : texto3, "texto4" : texto4})
