def soma_subtracao(x,y):
    if x==y:
        resultado=x+y 
    else:
        resultado=x-y
    return resultado
def main():
    x=60
    y=65      	
    resultado=soma_subtracao(x,y)
    print("resultado:",resultado)
main()

def ex2(x,y,funcao):
    if(funcao=="B"):
        return x*y
    else:
        return (2*x)+(2*y)
def main():
    x=3.5
    y=5
    funcao="P"
    resultado=ex2(x,y,funcao)
    print("O resultado é:", resultado)
main()

print("<<<LISTA DE EXÉRCÍCIOS>>>")
print("" "")
print("1-")
print("a.")
def maior(x,y):
    if(x>y):
        return(x)
    else:
        return(y)
def main():
    x=20
    y=21
    resultado=maior(x,y)
    print("O maior número é:",resultado)
main()

print("" "")
print("b.")


print("" "")
print("c.")


print("" "")
print("d.")
def absolut(x):
    if(x<0):
        return abs(x)
    else:
        return (x)
def main():
    x=(-7)
    resultado=absolut(x)
    print("o valor absoluto de (x) é:",resultado)
main()

print("" "")
print("e.")
def iguais(x,y):
    if(x==y):
        return "SIM"
    else:
        return "NAO"
def main():
    x=54
    y=54
    resultado=iguais(x,y)
    print("sao iguais?",resultado)
main()
