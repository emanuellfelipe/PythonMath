n = int(input("Defina o valor de n: "))

def fatorial(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

print(fatorial(n)) 
