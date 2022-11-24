class Pedido:
    def __init__(self) -> None:
        self.nombre=input('Introduce el nombre del comprador ').capitalize()
        self.tarjeta=input('Introduce el numero de la tarjeta ')
        self.fecha=input('Introduce la fecha de caducidad de la tarjeta ')
        self.cvv=input('Introduce el codigo secreto de la tarjeta ')
        self.pais=input('Introduce el pais donde se van a enviar los productos ').capitalize()
        self.municipio=input('Introduce el municipio donde se van a enviar los productos ').capitalize()
        self.calle=input('Introducee la calle donde se van a enviar los productos ').capitalize()
        self.telefono=input('Introduce un telefono de contacto ')
        self.email=input('Introduce un email para enviar la factura ')
    def MostrarDetalles(self):
        print(f'El nombre del comprador es {self.nombre}')
        print(f'El número de la tarjeta es {self.tarjeta}')
        print(f'El municipio del envío es {self.municipio}')
        print(f'La calle de la casa es {self.calle}')
        print(f'El teléfono de contacto es {self.telefono}')
        print(f'El email para el envío de la factura es {self.email}')
        print('Revise los datos antes de realizar la compra')
        eleccion=input('¿Son los datos correctos? S/N ').capitalize()
        if eleccion=="S":
            print('Pedido realizado con exito')
            print(f'Se ha enviado un sms al {self.telefono} para realizar un seguimiento de su pedido')
            print(f'Se ha enviado un email a {self.email} en el que se adjunta la factura')
            print('Muchas gracias por su compra')
        else:
            print('Compra no realizada') 

    def CalcularEnvio(self):
        if self.pais=='España':
            print(f'Al ser envío en España no se aplican costes de envío por lo que el precio es {precio1}€')
        else:
            precio2=precio1+15
            print(f'Al ser un envío fuera de España se aplicaran costes de envío por un valor de 15€ por lo que el precio final será de {precio2}€')
print('Bienvenido')
print('Que quieres hacer')
empezar=input('Iniciar sesion o Registrarse ').capitalize()
if empezar=="Iniciar sesion":
        usuario1=input('Dime tu nombre de usuario ')
        input('Dime tu contraseña ')
        print(f'Bienvenido {usuario1}')
else:
        input('Introduce tu email')
        usuario2=input('Introduce tu nombre de usuario')
        input('Introduce una contraseña ')
        print('Bienvenido')
print('Que quieres hacer ')
compra=[]
precios=[9.99,25.90,40,33.15,120,12.50,5.60,15.99,35.55,9.99,7.22]
precio1=0
bolsa=['Gorro','Camiseta','Sudadera','Pantalones','Zapatillas','Guantes','Calcetines','Pantalones cortos','Sudadera sin capucha',
'Ropa interior de hombre','Ropa interior de mujer']
print(f'Estos son los productos disponibles {bolsa}')

while True:
    print("1. Añadir productos")
    print("2. Eliminar productos")
    print("3. Mostrar lista de la compra")
    print("4. Realizar pedido")
    print("5. Salir de la aplicacion")
    opcion=input().capitalize()
    print()
    if opcion=="1":
        producto=input("introduce el producto que quieres comprar ").capitalize()
        if producto in bolsa:
            print("Producto añadido correctamente")
            compra.append(producto)
            indice=bolsa.index(producto)
            precio=precios[indice]
            precio1=precio1+precio
            round(precio1,3)
        else:
            print('Ese producto no existe')
    elif opcion=="2":
        producto=input("Introduce el producto que deseas eliminar de la lista ").capitalize()
        if producto not in compra:
                print('Ese producto no esta en la lista')
        else:
            compra.remove(producto)
            indice=bolsa.index(producto)
            precio=precios[indice]
            precio1=precio1-precio
            round(precio1,3)
    elif opcion=="3":
        print('Tienes los siguientes objetos en la lista')
        for e in compra:
            print(" -", e)
    elif opcion=="4":
        print(f'El total de los productos es {precio1}')
        print('A continucacion dame tus datos por favor')
        pedido1=Pedido()
        pedido1.CalcularEnvio()
        pedido1.MostrarDetalles()    
    elif opcion=="5":
        print('Hasta luego')
        break
    else:
        print('Ese apartado no existe,por favor introduzca un apartado valido')
