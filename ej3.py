class ItemsValiosos():
        def __init__(self, peso, nombre, precio, caducidad):
            self.peso = peso
            self.nombre = nombre
            self.precio = precio
            self.caducidad = caducidad
            print('Artefacto Valioso creado con exito!')
        
        def __str__(self):
            return 'Artefacto Valioso: {} con peso {} Kg, precio: {} euros, y caducidad: {}'.format(self.nombre, self.peso, self.precio, self.caducidad)
        
item1= ItemsValiosos(10, 'Artefacto 1', 100, '01/01/2020')
item2= ItemsValiosos(20, 'Artefacto 2', 200, '01/01/2020')
item3= ItemsValiosos(30, 'Artefacto 3', 300, '01/01/2020')

lista = [item1, item2, item3]
for i in lista: 
    print(i)

    def ordenar_lista(lista):
        lista.sort(key=lambda x: x.caducidad)
        print(lista)
    
    ordenar_lista(lista)

    def cambiar_precio(item, nuevo_precio):
        item.precio = nuevo_precio
        print('{} con nuevo precio de: {} euros'.format(item.nombre, item.precio))
    
    cambiar_precio(item1, 500)