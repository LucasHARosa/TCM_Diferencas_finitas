import matplotlib.pyplot as plt
import tcm2

matriz = tcm2.resolve()

plt.imshow(matriz, cmap='hot_r', interpolation='nearest', vmin=0, vmax=500, extent=[0, 5, 0, 5])
plt.ylabel("Y")
plt.xlabel("X")
plt.suptitle("Campo de temperatura       ")
plt.title(f'Número de nós: {200 ** 2}')
plt.colorbar(label="Temperature")
plt.show()