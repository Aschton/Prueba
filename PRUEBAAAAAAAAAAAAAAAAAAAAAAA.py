def menu():
    print("\nTOTEM AUTOMATICO RESERVAS STIKE")
    print("1. Reservar zapatillas")
    print("2. Buscar zapatillas reservadas")
    print("3. cancelar reserva")
    print("4. Salir")

def reservar(reservas):
    if len(reservas) >= 20:
        print("No se pueden hacer más reserva, Stocks agotados.")
        return
    nombre= input("Nombre del comprador: ")
    if nombre in reservas:
        print("nombre ya registrado.")
        return
    clave= input("Frase secreta:")
    if clave != "EstoyEnListaDeReserva":
        print("Frase incorrecta")
        return
    reservas[nombre]=1
    print(f"reserva realizada con exito para {nombre}.")

def buscar (reservas):
        nombre= input("nombre que desea buscar: ")
        if nombre in reservas:
            print(f"Zapatillas reservadas a nombre de {nombre} - {reservas[nombre]} par(es).")
            vip=input("desea Vip s/n?")
            reservas[nombre] = 2
            print("reserva actualizada a  VIP")
        else:
            print("No se encontraron reservas para ese nombre.")
        def ver_stocks(reservas):
            total=sum(reservas.values())
            print(f"Total de zapatillas reservadas: {total}")
            print(f"Pares disponibles: {20 - total}")
def cancelar(reservas):
    nombre = input("Ingrese el nombre de la reserva a cancelar: ")
    if nombre in reservas:
        del reservas[nombre]
        print(f"Reserva para {nombre} cancelada.")
    else:
        print("No se encontró una reserva con ese nombre.")
def main():
            reservas= {}
            while True:
                menu()
                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                    reservar(reservas)
                elif opcion == "2":
                    buscar(reservas)
                elif opcion == "3":
                    cancelar(reservas)
                elif opcion == "4":
                    print("Programa finalizado.")
                    break
                else:
                    print("Opción no válida, intente de nuevo.")
main() 
