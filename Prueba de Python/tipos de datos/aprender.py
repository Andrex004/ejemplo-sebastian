#"listas" [] con estas llaves se puede modificar la varible
listas = ["preciado", "monitel", True, 1.43]
#Tupla () Con estos parentesis la variable es fija
tupla = ("preciado", "montiel", True, 1.43 )

listas [2] = False

print (listas [2])
print (listas [1])

#creaando un diccionario (dict)
diccionario = {
    "nombre" : "Santiago",
    "edad" : 19,
    "Le gusta comer" : True,
    "no le gusta bañarse" : False
    }


print  (diccionario ["edad"] + 0.2)