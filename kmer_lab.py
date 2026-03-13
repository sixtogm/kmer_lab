# Generar k-mers a partir de una secuencia de DNA

# 1. Leer la secuencia de DNA
seq = input("DNA: ").upper()

# Validar que la secuencia no sea vacia
if not seq:
    print("No se ha ingresado una secuencia")
    exit(1)

# 2. Leer el valor de k
k = int(input("valor de k (int): "))

# 3. Recorrer la secuencia con una ventana de tamaño k
for i in range(len(seq) - k + 1):

    # 4. Extraer el k-mer de la posición actual
    kmer = seq[i:i+k] 

    # 5. Mostrar el k-mer
    print(f"Posicion {i} -> {kmer}")