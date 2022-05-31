import random as r
import matplotlib.pyplot as plt

temps = []
aux = []
aux2 = []
aux3 = []

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12,
     13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

y = []

for i in range(0, 46, 15):
    y.append(i)

for i in range(0, 25):
    if i >= 0 and i <= 3:
        temps.append(r.uniform(15, 18))
        temps.sort(reverse = True)

    elif i > 3 and i <= 15:
        aux.append(r.uniform(16, 45))
        aux.sort()

    elif i > 15 and i <= 23:
        aux2.append(r.uniform(18, 44))
        aux2.sort(reverse = True)

aux3 = temps + aux + aux2

print(aux3)

plt.plot(x, aux3, label="dados")
plt.ylabel("Temperaturas")
plt.xlabel("Horas do dia")
plt.title("Variação de temperatura em um dia")
plt.xticks(x)
plt.yticks(y)
plt.show()
