# Descripcion del proyecto
### 1. Problema

Generar todos los fragmentos consecutivos de longitud k (k-mers) a partir de una secuencia de DNA proporcionada por el usuario.

### 2. Datos de entrada

- una secuencia de DNA introducida por el usuario
- un número entero k que representa el tamaño del k-mer

### 3. Requisitos funcionales

- leer una secuencia de DNA
- leer el valor de k
- recorrer la secuencia
- generar todos los k-mers de longitud k
- mostrar cada k-mer en pantalla

### 4. Requisitos no funcionales

- el programa debe aceptar secuencias en mayúsculas o minúsculas.
- la secuencia debe convertirse a mayúsculas.
- el código debe ser legible y seguir convenciones básicas de estilo PEP8.

### 5. Algoritmo (Analisis y Diseño)

1. Leer la secuencia de DNA.
2. Leer el valor de k.
3. Recorrer la secuencia desde la posición 0 hasta len(seq) - k.
4. En cada posición, extraer un fragmento de longitud k.
5. Mostrar el k-mer generado.
6. Se evaluara cada k-mer para determinar cuál tiene mayor contenido GC.
7. Se mostrara la posicion del k-mer en la secuencias.