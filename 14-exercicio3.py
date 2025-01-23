from exercicio3 import Trip

trip0 = Trip("Lencoes maranhenses")
trip1 = Trip("Florianopolis")
trip2 = Trip("Gramado")
trip3 = Trip("Campos do Jordao")
trip4 = Trip("Caldas Novas")

print("E ai viajante. Temos algumas ofertas para você.\n")
traveler = input("Digite o seu nome para comecar\n")
print(
    f"{traveler}, temos 5 destinos que combinam com voce"
    """
      [0] - Lencoes maranhenses
      [1] - Florianopolis
      [2] - Gramado
      [3] - Campos do Jordão
      [4] - Caldas Novas
    """
)

choice = int(input("Selecione o destino da viagem\n"))
list_trip = [trip0, trip1, trip2, trip3, trip4]

for option in list_trip:
    if choice >= 5:
        print("Opção inválida")
        break
    if choice == list_trip.index(option):
        print(f"Sua viagem para {option.destiny} esta marcada")
        break