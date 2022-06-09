vetTemp = []

for i in range(6):
    vetTemp.append(float(input("Digite a temperatura: ")))

print("\nEm ordem de leitura:", vetTemp)
vetTemp.reverse()
print("\nEm ordem reversa da leitura:", vetTemp)
vetTemp.sort()
print("\nEm ordem crescente:", vetTemp)
vetTemp.sort(reverse = True)
print("\nEm ordem decrescente:", vetTemp) 

