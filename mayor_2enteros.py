#programa para verificar cual de dos enteros es el mayor

print("-------------------------------")
print("-----mayor 2 enteros-----")
print("-------------------------------")

# input
x = int(input("digite el valor de x: "))
y = int(input("digite el valor de y: "))

#processing
if x == y:
    print("los numeros son iguales...")
    
else:
    if x > y:
        mayor = x
    else:
        mayor = y        
        #output
    print("numero mayor: " + str(x) + " y " + str(y) + " es " + str(mayor))

