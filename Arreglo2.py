listaEst=[]
resp = "Si"
while (resp. upper()!= "NO"): #el upper es para las mayusculas
    tam= len(listaEst)#len es para el tamaño de un arreglo 
    print("Elementos guardados")
    nombres=input("Escriba el nombre del estudiante: ")
    listaEst. append(nombres)
    resp= input("Desea agregar mas? SI-NO")

for est in listaEst:
    print(est)