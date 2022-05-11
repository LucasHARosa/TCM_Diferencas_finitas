import matplotlib.pyplot as plt
import tcm2

matriz = tcm2.resolve()

espace = []
for i in range(200):
    espace.append(i)
#plotagem do gráfico
plt.plot(espace, matriz[160])
plt.title('Temperatura X (Eixo x)')
plt.suptitle('Perfil de temperatura (Matriz 200x200)')
plt.ylabel('Temperatura')
plt.xlabel('Eixo (x) com y = [160]')
plt.show()