class Ejercicios:

    def __init__(self):
        pass
        
    def parImpar(self, numero):
        if numero % 2 == 0:
            print("{} es Par".format(numero))
        else:
            print("{} es Impar".format(numero))
            

    def perfecto(self, numero):
        acu=0
        for i in range(1, numero):
            if numero % i == 0:
                acu = acu+i
        if acu == numero:
            print("{} es Perfecto".format(numero))
        else:
            print("{} no es Perfecto".format(numero))


             
    def perfecto2(self, numero):
        acu=0
        for i in range(1, numero):
            if numero % i == 0:
                acu = acu+i
        return acu

            
ejer = Ejercicios()
# num = int(input("Ingrese un numero: "))
# print("Llamada 1")
# resp= ejer.perfecto2(num)
# if num == resp:
#     print("{} es perferto".format(num))
# else:
#     print("{} no es perfecto".format(num))
# input()
lista = [3,5,6,8,28]
print("llamada 2")
perfetos = []
for num in lista:
    if ejer.perfecto2(num) == num:
        perfetos.append(num)
print(perfetos)