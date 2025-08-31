#Crie uma calculadora que tenha

# 1. Menus
# 2. Soma / Subtrcao / Divisao / Multiplicacao(FEITO!)
# 3. Potenciacao / raiz / porcentagem(FEITO!)
# 4. Histórico de cálculos
# 5. Mostrar as últimas operações realizadas e permitir repetir alguma delas.
# 6. Tratamento avançado de erros
# 7. Entrada inválida (ex: abc)
# 8. Tatar Divisão por zero (FEITO!)



menu = ""
while menu != 's':
    print('Calculadora:')
        
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Potenciação')
    print('6 - Radiciação')
    print('7 - Porcentagem')
    print('8 - Sair ')
    opçao = int(input('Escolha uma das opções: '))

    if opçao == 1:
        n1=float(input('Digite um numero: '))
        n2= float(input('Digite um numero: '))
        resultado = n1 + n2
        print(f'O resultado é {resultado}')

    elif opçao == 2:
        n1=float (input('Digite um numero: '))
        n2= float(input('Digite um numero: '))
        resultado = n1 - n2
        print(f'O resultado é {resultado}')
    
    elif opçao == 3:
        n1=float (input('Digite um numero: '))
        n2= float(input('Digite um numero: '))
        resultado = n1 * n2
        print(f'O resultado é {resultado}')
    
    elif opçao == 4:
        n1=float (input('Digite um numero: '))
        n2= float(input('Digite um numero: '))
        if n2 != 0:
            resultado = n1 / n2
            print(f'O resultado é {resultado}')
        else:
            print('Não é possivel dividir por zero')

    elif opçao == 5:
        n1=float (input('Digite um numero: '))
        n2= float(input('Digite um numero: '))
        resultado = n1**n2
        print(resultado)

    elif opçao == 7:
        valor= int(input('Digite o valor:'))
        porcento = int(input('Digite a porcentagem:'))
        resultado = ((valor * porcento)/100)
        print(resultado)

    elif opçao == 8:
        menu = "s"

    if opçao == 0 or opçao >= 9:
        print('Operação Invalida')
