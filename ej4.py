def main():
  
#Creamos una función que nos de falso si la mochila esta vacía.
  def usar_la_fuerza(mochila, numero_objetos=0):
    if not mochila:
      return False, numero_objetos

    #Sacamos de la mochila el primer objeto que haya
    objeto = mochila[0]
    mochila = mochila[1:]

    #Usamos una función recursiva para ver si encuentra el sable de luz o no, si no lo encuentra
    #seguirá sacando objetos hasta encontrarlo.
    if objeto == "sable de luz":
      return True, numero_objetos
    return usar_la_fuerza(mochila, numero_objetos + 1)

  #Ahora comprobamos si está el sable de luz
  #también se muestra el número de elementos extraídos hasta encontrarlo.
  lista = ["espada láser","botella de agua","sable de luz", "bocadillo"]
  print(usar_la_fuerza(lista))

if __name__=='__main__':
    main()
         