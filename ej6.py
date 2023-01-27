from hash import *
import random

def generador():
    lista_naves = []
    for i in range(2000):
        naves = random.choice(["FL", "TF", "TK"," CT", "FN"," FO"])
        numero = random.randint(1000,9999)
        nave = numero + "-" + naves
        lista_naves.append(nave)
    return lista_naves, naves, numero


naves, nav, numero = generador()
hash1 = crear_tabla(len(naves))
hash2 = crear_tabla(len(naves))

for nave in naves:
    agregar(hash1, nave[:1], convert="")
    agregar(hash2, nave[3:], convert="")


    if buscar(hash1,"FN")!=None or buscar(hash2,"2187")!=None:
        quitar(hash1,"FN")
        quitar(hash2,"2187")

    nuevas_naves = []
    for i in range(len(nav)):
        if numero[i]=="781" or numero[i]=="537":
            nuevas_naves.append(naves[i])

    print(f"Las naves son: {nuevas_naves}")


legion_ct = []
legion_tf = []
for i in range(len(nav)):
    if nav[i]=="CT":
        legion_ct.append(naves[i])
    elif nav[i]=="TF":
        legion_tf.append(naves[i])


print(f"Las naves que contienen CT son: {legion_ct}")
print(f"Las naves que contienen CT son: {legion_tf}")