a =  int(input("Insira o Valor de a: "))
n =  int(input("Insira o Valor de n: "))

def exp(a, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 
    elif n % 2 == 0:
        rest = exp(a, n // 2)
        return rest * rest
    else:
        return a * exp(a, n - 1)

print(exp(a, n))
