import matplotlib.pyplot as plt

#tempo de execucao para cada malha
tempo = [1.48,5.57,8.97,31.98]
#quantidade de nos presentes em cada malha
no = [2500,6400,10000,40000]
#plotagem do gráfico
plt.plot(no,tempo)
plt.title('Tempo computacional (s) X Número de Nós')
plt.xlabel('Número de nós (unid.)')
plt.ylabel('Tempo de execução computacional (segundos)')
plt.show()