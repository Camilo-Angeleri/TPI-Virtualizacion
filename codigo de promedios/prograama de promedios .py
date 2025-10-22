lista_promedio=[]
suma=0
print("------------------------\nIngresa tus notas para calcular el promedio. Para finalizar el proceso, introduce 'stop'")
while True:
   contador=len(lista_promedio)+1 #empieza siempre con uno menos, asi que con el mas 1 se soluciona
   entrada=input(f"(Nota {contador}): ").strip()
   if str(entrada).isnumeric()==True and 10>=int(entrada)>=0:
       entrada=int(entrada)
       suma=suma+entrada
       lista_promedio.append(entrada)
       promedio=suma/len(lista_promedio)
   elif entrada=="Stop" or entrada=="stop":
       break
   else:
       print("Introduce solo numeros enteros sin signos positivos o negativos.\n------------------------")
print("------------------------\nFin!\n------------------------")
if len(lista_promedio)>0:
   print("Tus notas: ")
   for i in range (len(lista_promedio)):
       print(f"{lista_promedio[i]}\n-")
   print(f"Promedio total: {promedio}")
   print("------------------------")
