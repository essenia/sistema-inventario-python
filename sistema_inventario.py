class Producto:
  def __init__(self,nombre :str, precio: float, cantidad: int):
     # Validaciones

     if not nombre or not nombre.strip():
        raise ValueError('el nombre no puede estar vacío..')
     if precio < 0 :
        raise ValueError('el precio debe ser mayor o igual que cero')
    
     if cantidad < 0 :
        raise ValueError('la cantidad debe ser mayor o igual que cero ')
    
     self.nombre = nombre
     self.precio = float(precio)
     self.cantidad = int(cantidad)

# Actualizar precio

  def actualizar_precio(self, nuevo_precio: float):
     if nuevo_precio < 0 :
       raise ValueError('El precio debe ser mayor o igual que cero.')
     self .precio =  float(nuevo_precio)
# Actualizar cantidad
  
  def actualizar_cantidad( self, nueva_cantidad : int):
     if nueva_cantidad < 0 :
       raise ValueError('la cantidad debe ser mayor o igual que cero')
     self.cantidad = int(nueva_cantidad)

# funcion para calcular el valor total
  def calcular_valor_total(self): 
    return self.precio * self.cantidad


# funcion mostrar la información del producto
  def __str__(self): 
   return (
     f"Producto : { self.nombre}  €\n"
     f"Precio : { self.precio:.2f}  €\n"
     f"Cantidad : { self.cantidad}  €\n"
     f"Valor Total :   { self.calcular_valor_total():.2f}  € \n"


  )



class Inventario:
  
  def __init__(self):
    #   lista vacía para guardar los productos 
      self.productos = []
  
    # Añadir producto

  def agregar_producto(self, producto):
      if not isinstance(producto, Producto):
          raise TypeError("Solo se pueden agregar objetos Producto.")

      self.productos.append(producto)
       
  # Buscar producto por nombre

  def buscar_producto(self, nombre):
     
      if not isinstance(nombre, str):
          raise TypeError("el nombre debe ser texto.")
      
      for producto in self.productos :
          if producto.nombre.lower() == nombre.lower():
            return producto
      return None 

  def calcular_valor_inventario(self):
        total = 0

        for producto in self.productos:
            total += producto.calcular_valor_total()

        return total   
  def listar_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
            return

        for producto in self.productos:
            print("------------------------")
            print(producto)


def menu_principal(inventario):
   
   while True:
        print("\n====== SISTEMA DE INVENTARIO ======")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Calcular valor total del inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        try:

            if opcion == "1":
                nombre = input("Nombre del producto: ")

                precio = float(input("Precio del producto (€): "))

                cantidad = int(input("Cantidad del producto: "))

                producto = Producto(nombre, precio, cantidad)

                inventario.agregar_producto(producto)

                print("Producto agregado correctamente.")

            elif opcion == "2":
                nombre = input("Ingrese el nombre del producto a buscar: ")

                producto = inventario.buscar_producto(nombre)

                if producto:
                    print("\nProducto encontrado:")
                    print(producto)
                else:
                    raise ValueError("Producto no encontrado.")

            elif opcion == "3":
                inventario.listar_productos()

            elif opcion == "4":
                total = inventario.calcular_valor_inventario()

                print(
                    f"Valor total del inventario: {total:.2f} €"
                )

            elif opcion == "5":
                print("Saliendo del sistema...")
                break

            else:
                print("Opción no válida.")

        except ValueError as e:
            print(f"Error de valor: {e}")

        except TypeError as e:
            print(f"Error de tipo de dato: {e}")

        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == "__main__":

    inventario = Inventario()

    menu_principal(inventario)
      



# if __name__ == "__main__":
#     producto = Producto("Laptop", 1200.50, 5)
#     print(producto)

#     producto.actualizar_precio(1300.00)
#     producto.actualizar_cantidad(7)

#     print("\nDespues de la actualización : ")
#     print(producto)
  