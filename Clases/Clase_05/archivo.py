
##
## Crear archivo.
##

##archivo=open("Curso1.txt","w")
##archivo.close()

archivo=open("Curso1.txt","r")
print(archivo)
lineas=archivo.readlines()
print("\n ============ \n")
print(lineas)

print("\n ============ \n")
for i in lineas:
    print(i)

print("\n ============ \n")

for i in lineas:
    print(i[:-1])

print("\n ============ \n")
##print(archivo.readlines())
##print("Nuevo Volcado de Datos")
##print(archivo.readlines())
##print("Nuevo Volcado de Datos final")
archivo.close()



