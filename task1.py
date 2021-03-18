import time

nombrearch = input("Teclea el nombre del archivo: ")
print(nombrearch)
contmax = int(input("Cuenta máxima: "))
i=0
while i<= contmax:
 f=open(nombrearch, "a")
 time.sleep(1)
 f.write(str(i))
 f.write("/n")
 f.close()
 i+=1
