# Encontrar el número que falta.

lista = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(lista)-1):
    suma = lista[i] + lista[i+1]

print(suma)

lista_num_faltante = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(lista_num_faltante)-1):
    suma_faltante = lista_num_faltante[i] + lista_num_faltante[i+1]

print(suma_faltante)

if suma_faltante == suma:
    print("\nNo hay ningun número faltante\n")
    
else:
    numero_faltante = suma - suma_faltante
    
    print(f"\nEl número faltante es {numero_faltante}")