a =  int(input("Insira o Valor de a: "))
b =  int(input("Insira o Valor de b: "))


def mdc(a, b):
    if a == 0 and b == 0:
        return "O MDC é indeterminado para a = 0 e b = 0"

    if b == 0:
        return abs(a)

    return mdc(b, a % b)

resultado = mdc(a, b)
print(resultado)

