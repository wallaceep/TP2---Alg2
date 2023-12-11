import matplotlib.pyplot as plt

# Dados para o primeiro conjunto
datasets1 = ['eil51', 'berlin52', 'st70', 'eil76', 'pr76', 'rat99', 'kroA100', 'kroB100', 'kroC100', 'kroD100']
distances1 = [3089.29, 50641.11, 9430.50, 5851.25, 1596792.61, 28070.01, 330014.62, 346512.31, 376218.70, 392156.28]
memory1 = [0.61, 0.16, 0.12, 0.0, 0.13, 0.0, 0.0, 0.02, 0.03, 0.0]
time1 = [3.11, 3.29, 3.11, 3.23, 3.09, 3.20, 3.62, 3.60, 4.02, 4.13]

# Dados para o segundo conjunto
datasets2 = ['eil51', 'berlin52', 'st70', 'eil76', 'pr76', 'rat99', 'kroA100', 'kroB100', 'kroC100', 'kroD100']
distances2 = [597.34, 9908.05, 839.40, 685.25, 141621.93, 1700.28, 25701.04, 25623.10, 26443.05, 26053.55]
memory2 = [0.13, 0.01, 0.08, 0.04, 0.00, 0.16, 0.01, 0.00, 0.00, 0.00]
time2 = [0.11, 0.10, 0.11, 0.11, 0.11, 0.11, 0.12, 0.11, 0.11, 0.12]

# Limiar
limiar = [426, 7542, 675, 538, 108159, 1211, 21282, 22141, 20749, 21294]

# Gráfico de Distância
plt.figure(figsize=(10, 6))
plt.plot(datasets1, distances1, marker='o', label='Conjunto 1')
plt.plot(datasets2, distances2, marker='o', label='Conjunto 2')
plt.plot(datasets1, limiar, linestyle='--', color='red', label='Limiar')
plt.xlabel('Dataset')
plt.ylabel('Distância')
plt.title('Comparação de Distância')
plt.legend()
plt.tight_layout()
plt.savefig('distancia_comparison.png')
plt.show()

# Gráfico de Memória
plt.figure(figsize=(10, 6))
plt.plot(datasets1, memory1, marker='o', label='Conjunto 1')
plt.plot(datasets2, memory2, marker='o', label='Conjunto 2')
plt.xlabel('Dataset')
plt.ylabel('Memória')
plt.title('Comparação de Memória')
plt.legend()
plt.tight_layout()
plt.savefig('memoria_comparison.png')
plt.show()

# Gráfico de Tempo
plt.figure(figsize=(10, 6))
plt.plot(datasets1, time1, marker='o', label='Conjunto 1')
plt.plot(datasets2, time2, marker='o', label='Conjunto 2')
plt.xlabel('Dataset')
plt.ylabel('Tempo')
plt.title('Comparação de Tempo')
plt.legend()
plt.tight_layout()
plt.savefig('tempo_comparison.png')
plt.show()
