#!/urs/bin/python

#guardar en ñla carpeta de proyecto


# las funciones en python parten con def...
def funcion_tonta(nombre):
    separador =" "
    print(separador.join(("hola",nombre, "eres un tonto")))
#calcular el digito veriifcador 

def digito_verificador (rut_sin_digito):
    digito = ""
    multiplo = 0
    acumulador = 0
    contador = 2
    while rut_sin_digito > 0 :
        multiplo= (rut_sin_digito % 10) * contador
        acumulador= acumulador +multiplo
        rut_sin_digito= rut_sin_digito // 10 #division entera colocado con dos //
        contador= contador + 1
        if contador == 8:
            contador=2
    digito=11 -(acumulador % 11)
    if digito ==10:
        digito='k'
    if digito== 10:
        digito=0
    return digito
mi_rut = 19345064
print("-".join((str(mi_rut),str(digito_verificador(mi_rut)))))


 #llamamos a la funcion directamente...
funcion_tonta("nicolas")