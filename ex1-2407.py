# O matemático Malbataam precisa de um programa para calcular o valor de uma função do primeiro grau ou uma função do segundo grau de 
# acordo com o que o usuário solicitar.  

#   Se o usuário escolher calcular uma função do primeiro grau, ele deve passar os parâmetro A, B e o valor de X e o programa deve 
#   calcular f(x) = ax + b.
#   Por exemplo, se o usuário escolher A=2 , B=3 e X=1 então o programa deve calcular o valor de f(x) = 2*1 + 3 ou seja deve retornar 5
  
#   Se o usuário escolher calcular uma função do segundo grau, ele deverá passar os valores dos parâmetros A, B, C e X e o 
#   programa deve calcular f(x) = Ax**2+ Bx + C.
#   Por exemplo se o usuário escolher A=1, B=3, C=2 e X=1 então o programa deve calcular o valor de f(x)=1*[(1)**2]+3*1+2 ou 
#   seja deve retornar 6

# obs.: Deverá ser criado funções no programa

def funcaoPrimeiroGrau(a, b, x):
    n1 = int(a)
    n2 = int(b)
    n3 = int(x)
    total = (n1*n2+n3)
    return total

def funcaoSegundoGrau(a,b,c,x):
    n1 = int(a)
    n2 = int(b)
    n3 = int(c)
    n4 = int(x)


    return n1*(n4**2) + n2*n4 + n3

p = 's'

while p == 's':
    print('Qual tipo de função deseja encontra o resultado')
    print('1 - Função do primeiro grau')
    print('2 - Função do segundo grau')

    i = int(input('Escolha uma opção: '))

    n1 = input('Digite o valor de A: ')
    n2 = input('Digite o valor de B: ')

    if(i == 2):
        n3 = int(input('Digite o valor de C: '))
        n4 = int(input('Digite o valor de X: '))
        total = int(funcaoSegundoGrau(n1, n2, n3, n4))
        print(f'Valor total é {total}')

    elif(i == 1):
        n3 = input('Digite o valor de X: ')
        total = int(funcaoPrimeiroGrau(n1, n2, n3))
        print(f'Valor total é {total}')

    p = input('Deseja continuar(S/N) ').lower()

    if(p != 's'):
        print('Ok, Até mais!')

