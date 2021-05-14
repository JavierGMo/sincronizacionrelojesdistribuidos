def algoritmo(horaServerCompleta=[15, 0, 0], horaCliente = [14, 25, 27], latencia=1):
    horaActualizada = horaServerCompleta[0] + (horaCliente[0] - horaCliente[0])//2
    minutosActualizados = horaServerCompleta[1] +(horaCliente[1] - horaCliente[1]+latencia)//2
    segundosActualizados = horaServerCompleta[2] + (horaCliente[2] - horaCliente[2])//2
    return ('Hora actualizada : {}:{}:{}'.format(horaActualizada, minutosActualizados, segundosActualizados))


horasClientes = [
    ([14, 25, 27], 1),
    ([16, 15, 36], 7),
    ([12, 35, 41], 5),
    ([15, 0, 0], 5),
    ([12, 40, 38], 10),
]
horaServerCompleta=[15, 0, 0]
print('Hora server : {}:{}:{}'.format(horaServerCompleta[0], horaServerCompleta[1], horaServerCompleta[2]))
for hora in horasClientes:
    print(algoritmo(horaCliente=hora[0], latencia=hora[1]))