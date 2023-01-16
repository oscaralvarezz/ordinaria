def usar_la_fuerza(mochila, num_objetos=0):
  # En el caso de que la mochila este vacia nos da falso
  if not mochila:
    return False, num_objetos

  # Obtenemos el primer objeto
  objeto = mochila[0]
  mochila = mochila[1:]

  # Si el sable encontramos el objeto si no utilizamos recursividad para ver si esta
  if objeto == "sable de luz":
    return True, num_objetos
  return usar_la_fuerza(mochila, num_objetos + 1)

# Comprobacion
if __name__=="__main__":
  lista = ["champiñon","europa","sable de luz", "la nueva liga"]
  print(usar_la_fuerza(lista))