### Durante la creacion de este codigo el asistente "TutorPy: Tu guía en Python paso a paso" de la compañia ChatGPT, creado por Lic. Salgado fue utilizado en las siguientes ocasiones:

1. Se le pregunto por una correcion a la manera de guardar los datos más importantes del GC de mayor valor.

```python 
# 5. Mostrar el k-mer print(f"Posicion {i} -> {kmer} (GC={sum_gc})") 
if sum_gc == k: 
best_sum_gc=sum_gc 
best_kmer=kmer 
bk_position=i 
print(f"Best so far -> {best_kmer} (GC={best_sum_gc})") 
else: 
if sum_gc > 0: 
best_sum_gc=sum_gc 
best_kmer=kmer 
bk_position=i print(f"Best so far -> {best_kmer} (GC={best_sum_gc})")
````

Obteniendo la siguiente sugerencia:

````python
# Comparar con el mejor encontrado  
if  sum_gc  >  best_sum_gc:  
best_sum_gc  =  sum_gc  
best_kmer  =  kmer  
bk_position  =  i  
print(f"Best so far -> {best_kmer} (GC={best_sum_gc})")
````

Con base a la cual fue modificado el programa.
