moedas = (5, 10, 2)
total_moedas = moedas[0] + moedas[1] + moedas[2]
valor = (5, 3, 1)
valor_total = 0

for i in range(len(moedas)):
    valor_total += moedas[i] * valor [i]

print("Moedas de cada tipo: " + str(moedas[0]) + " ouro " + str(moedas[1]) + " prata " + str(moedas[2]) + " bronze ")
print("Total de Moedas: " + str(total_moedas))
print("Valor por tipo: " + str(valor[0]) + " ouro " + str(valor[1]) + " prata " + str(valor[2]) + " bronze ")
print("Valor total: " + str(valor_total))