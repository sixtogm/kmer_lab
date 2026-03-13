# Generar k-mers a partir de una secuencia de DNA

# 1. Leer la secuencia de DNA
seq = input("DNA: ").upper()

# Validar que la secuencia no sea vacia
if not seq:
    print("No se ha ingresado una secuencia")
    exit(1)

# 2. Leer el valor de k
k = int(input("valor de k (int): "))
# (se inicializa best_sum_gc para la comparacion de mas adelante)
best_sum_gc = 0
# (se crea el señalador con base en el tamaño del kmer)
señalador = "^"*k

# 3. Recorrer la secuencia con una ventana de tamaño k
for i in range(len(seq) - k + 1):

    # 4. Extraer el k-mer de la posición actual
    kmer = seq[i:i+k] 
    count_g = kmer.count("G")
    count_c = kmer.count("C")
    sum_gc = (count_c+count_g)


    # 5. Mostrar el k-mer y calcular el que tenga la mayor composicion de gc, su posicion y su composicion
    print(f"{seq}")
    print(f"{señalador} Posicion {i} -> {kmer} (GC={sum_gc})")
    # va moviendo el señalador un "espacio" a la derecha con cada vuelta del for.
    señalador = " " + señalador
    if sum_gc >= best_sum_gc:
       best_sum_gc = sum_gc
       best_kmer = kmer
       bk_position = i
       print(f"Best so far -> {best_kmer} (GC={best_sum_gc})")
    else:
        print(f"Best so far -> {best_kmer} (GC={best_sum_gc})")
# 6. Mostrar el kmer con mayor GC y su posicion.
print(f"Final best k-mer: {best_kmer}")
print(f"Position: {bk_position}")
print(f"GC count: {best_sum_gc}")


