print()
print()

# Cuadrado relleno
size= 5
for i in range(0,size):
    for j in range(0,size):
        print("* ", end="")
    print()

print()
print()

#Cuadrado hueco
size= 5
for i in range(0,size):
    for j in range(0,size):
        if i==0 or i==size-1 or j==0 or j==size-1:
            print("*", end=" ")
        else:
            print(' ',end=' ')
    print()

print()
print()

#Traingulo a la izquierda
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("* ", end="")
    print()


print()
print()

#Traingulo a la derecha
n=5
for i in range(n):
    for j in range(1,n-i):
        print(" ", end=" ")
    for k in range(n-i,n+1):
        print("*", end=" ")
    print()




print()
print()

#Traingulo hueco a la izquierda
n=5
for i in range(1,n+1):
    for j in range(i):
        if j==0 or j==i-1:
            print("*", end=" ")
        else:
            if i!=n:
                print(" ", end=" ")
            else:
                print("*", end=" ")
    print()


print()
print()

#Traingulo a la derecha invertido
n=5
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()


print()
print()

#Piramide
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for k in range(2*i+1):
        print("*", end=" ")
    print()



print()
print()

#Piramide Hueca
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for k in range(2*i+1):
        if k==0 or k==2*i:
            print("*", end=" ")
        else: 
            if i == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()

print()
print()

#Rombo
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for k in range(2*i+1):
        print("*", end=" ")
    print()
for i in range(n-1):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(2*(n-i-1)-1):
        print("*", end=" ")
    print()
    


print()
print()

#Rombo hueco
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for j in range(2*i+1):
        if j==0 or j==2*i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(n-1):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(2*(n-i-1)-1):
        if j==0 or j==2*(n-i-1)-2:
            print("*", end=" ")
        else:
             print(" ", end=" ")
    print()
