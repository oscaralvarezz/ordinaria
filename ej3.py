class ItemsValiosos():
        def __init__(self, peso, nombre, precio, caducidad):
            self.peso = peso
            self.nombre = nombre
            self.precio = precio
            self.caducidad = caducidad
            print('Un Artefacto Valioso se ha creado con exito!')
        
        def __str__(self):
            return 'El Artefacto Valioso: {} con un peso de {} Kg, un precio de: {} euros, y una fecha de caducidad: {}'.format(self.nombre, self.peso, self.precio, self.caducidad)
        
elemento1= ItemsValiosos(10, 'Artefacto 1', 100, '01/01/2020')
elemento2= ItemsValiosos(20, 'Artefacto 2', 200, '01/01/2020')
elemento3= ItemsValiosos(30, 'Artefacto 3', 300, '01/01/2020')

lista = [elemento1, elemento2, elemento3]
for i in lista: 
    print(i)

    def ordenar_lista(lista):
        lista.sort(key=lambda x: x.caducidad)
        print(lista)
    
    ordenar_lista(lista)

    def cambiar_precio(item, nuevo_precio):
        item.precio = nuevo_precio
        print('{} con nuevo precio de: {} euros'.format(item.nombre, item.precio))
    
    cambiar_precio(elemento1, 500)