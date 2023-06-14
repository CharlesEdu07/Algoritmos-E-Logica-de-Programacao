vet_temp = []
hours = []
temp_aux = []

soma_temp = 0
cont = 0

for i in range(8):
    print("\nDigite a temperatura às", i * 3, "horas")
    temp = float(input("> "))
    vet_temp.append(temp)

for i in vet_temp:
    soma_temp += i

media = soma_temp / len(vet_temp)

print("\nTemperatura média: %.1f" % (media))

for i in vet_temp:
    if i > media:
        cont += 1
        temp_aux.append(i)
        hours.append(vet_temp.index(i) * 3)

print("A temperatura ficou", cont, "vezes acima da média")
print("Nos horários:", hours)
print("\nTemperaturas acima da média:", temp_aux)
