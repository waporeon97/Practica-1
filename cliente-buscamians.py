import socket
import os
import numpy as np


HOST = "192.168.56.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
buffer_size = 1024
def menu():
    os.system("cls")
    print("Selecciona la dificultad del juego")
    print("\t1 - Principiante")
    print("\t2 - Avanzado")
    print("\t3 - Salir")
def construir_tablero (n):
    m = np.zeros((n,n))
    for i in range(len(m)-1):
        m[0][i+1]=i+1
    for i in range(len(m)-1):
        m[i+1][0] = i + 1
    return m
def tirarx():
    x = input("inserta el numero de columna >> ")
    return x
def tirary():
    y = input("inserta el numero de fila >> ")
    return y
def dibujatablero(M):
    print (M)

def minar():
    m = TCPClientSocket.recv(buffer_size)
    m = m.decode('ascii')

    print(m)
def principiante() :
    print("Has seleccionado la dificultad de principiante\n\n")
    n = 10

    t = construir_tablero(n)
    dibujatablero(t)
    for i in [0,1,n]:
        x = tirarx()
        equis = bytes(x, encoding="ascii")
        TCPClientSocket.sendall(equis)
        y = tirary()
        ye = bytes(y, encoding="ascii")
        TCPClientSocket.sendall(ye)
        flag = TCPClientSocket.recv(buffer_size)
        flag = flag.decode('ascii')
        if flag == "1":
            print("perdiste")
            minar()
            return 0
        elif flag == "0":
            t[int(y)][int(x)] = 1
            print(t)
def avanzado() :
    print("Has seleccionado la dificultad de principiante\n\n")
    n = 17

    t = construir_tablero(n)
    dibujatablero(t)
    for i in [0,1,n]:
        x = tirarx()
        equis = bytes(x, encoding="ascii")
        TCPClientSocket.sendall(equis)
        y = tirary()
        ye = bytes(y, encoding="ascii")
        TCPClientSocket.sendall(ye)
        flag = TCPClientSocket.recv(buffer_size)
        flag = flag.decode('ascii')
        if flag == "1":
            print("perdiste")
            minar()
            return 0
        elif flag == "0":
            t[int(y)][int(x)] = 1
            print(t)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    TCPClientSocket.connect((HOST, PORT))


    while True:
        # Mostramos el menu
        menu()

        # solicituamos una opción al usuario
        opcionMenu = input("Selecciona una opcion >> ")
        if (opcionMenu == "1"):
            aux = bytes(opcionMenu, encoding="ascii")
            TCPClientSocket.sendall(aux)
            principiante()
        elif (opcionMenu == "2"):
            aux = bytes(opcionMenu, encoding="ascii")
            TCPClientSocket.sendall(aux)
            avanzado()
        elif (opcionMenu == "3"):
            aux = bytes(opcionMenu, encoding="ascii")
            TCPClientSocket.sendall(aux)
            break

        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")

    #TCPClientSocket.sendall(b"Hello TCP server")
    #data = TCPClientSocket.recv(buffer_size)
    #print("Recibido,", repr(data), " de", TCPClientSocket.getpeername())
