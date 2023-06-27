a =  int(input("Insira o Valor de a: "))
n =  int(input("Insira o Valor de n: "))
m =  int(input("Insira o Valor de m: "))

def exp_mod(a, n, m):
    if m < 2:
        raise ValueError("É impossível calcular com m < 2")
    if n == 0:
        if a == 0:
            raise ValueError("É impossível calcular 0^0 mod m")
        return 1 % m
    if n % 2 == 0:
        x = exp_mod(a, n // 2, m)
        return (x * x) % m
    else:
        x = exp_mod(a, (n - 1) // 2, m)
        return (a * x * x) % m


resultado = exp_mod(a, n, m)
print(resultado)
