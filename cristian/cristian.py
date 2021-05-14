from datetime import datetime
import socket
import sys

class Cristian:
    
    tiempo = ''
    hora = 0
    minutos = 0
    segundos = 0

    auxHora = 0
    auxMinutos = 0
    auxSegundos = 0
    auxTiempo = ''

    intervaloSC = 0
    
    server = ''
    port=0
    def __init__(self, server='localhost', port=3000, intervaloSC = 0):
        #Socket config
        self.server = server
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.server, self.port))
        #config Intervalo
        self.intervaloSC = intervaloSC
        
        
    def peticionManual(self):
        try:
            pass
        finally:
            self.sock.close()
        
    def peticion(self):
        try:
            self.hora = datetime.now().hour
            self.minutos = datetime.now().minute
            self.segundos = datetime.now().second
            self.tiempo = '{}:{}:{}'.format(self.hora, self.minutos, self.segundos)
            
            message = '{}'.format(self.tiempo)
            
            self.auxHora = self.hora
            self.auxMinutos = self.minutos
            self.auxSegundos = self.segundos
            self.auxTiempo = self.tiempo

            #Enviamos la hora de nuestro server cliente
            self.sock.sendall(message.encode())
            
            #Recibimos la data
            data = self.sock.recv(32)
            
            
            self.tiempo = data.decode()
            tiempoServer = self.tiempo.split(':')

            # Tt: marca la hora de llegada del mensaje del server, para verificar la hora
            llegadaDelServerTt = datetime.now()

            self.__algoritmoCristian(llegadaDelServerTt, tiempoServer)
            
            print('Hora del server : {}'.format(data))
            print('Hora sincronizada : {}:{}:{}'.format(self.auxHora, self.auxMinutos, self.auxSegundos))
        finally:
            self.sock.close()
    def __algoritmoCristian(self, llegadaDelServerTt, tiempoServer):
        #El tiempo de ahora
        marcaDeHoraAhora = llegadaDelServerTt.hour
        marcaDeMinutosAhora = llegadaDelServerTt.minute
        marcaDeSegundos = llegadaDelServerTt.second

        # Operacion de RTT = (Tt-Tr)
        marcaDeHoraAhora += (-self.auxHora)
        marcaDeMinutosAhora += (-self.auxMinutos)
        marcaDeSegundos += (-self.auxSegundos)

        marcaDeHoraAhora /= 2
        marcaDeMinutosAhora /= 2
        marcaDeSegundos /= 2

        #Operacion Tutc server + RTT/2 = Tcliente
        self.hora = int(tiempoServer[0])+marcaDeHoraAhora
        self.minutos = int(tiempoServer[1])+marcaDeMinutosAhora
        self.segundos = int(tiempoServer[2])+marcaDeSegundos