#Crie uma calculadora que tenha

# 1. Menus
# 2. Soma / Subtrcao / Divisao / Multiplicacao(FEITO!)
# 3. Potenciacao / raiz / porcentagem(FEITO!)
# 4. Histórico de cálculos(FEITO!)
# 5. Mostrar as últimas operações realizadas e permitir repetir alguma delas.
# 6. Tratamento avançado de erros
# 7. Entrada inválida (ex: abc)(FEITO!)
# 8. Tatar Divisão por zero (FEITO!)



menu = ""
historico = []
while menu != 's':
    print("\n")

    print('Menu da Calculadora \n')    
    print(' 1 -  Adição')
    print(' 2 -  Subtração')
    print(' 3 -  Multiplicação')
    print(' 4 -  Divisão')
    print(' 5 -  Potenciação')
    print(' 6 -  Radiciação')
    print(' 7 -  Porcentagem')
    print(' 8 -  Histórico de calculos')
    print(' 9 -  Repetir operação do histórico')
    print(' 10 - Sair \n')
    
    opçao = int(input('Escolha uma das opções: '))
    

    if opçao == 1:
        n1 = float(input('Digite um numero: '))
        n2 = float(input('Digite um numero: '))
        resultado = n1 + n2
        print(f'O resultado é {resultado}')
        historico.append(f"{n1} + {n2} = {resultado}")

    elif opçao == 2:
        n1 = float (input('Digite um numero: '))
        n2 = float(input('Digite um numero: '))
        resultado = n1 - n2
        print(f'O resultado é {resultado}')
        historico.append(f"{n1} - {n2} = {resultado}")
    
    elif opçao == 3:
        n1 = float (input('Digite um numero: '))
        n2 = float(input('Digite um numero: '))
        resultado = n1 * n2
        print(f'O resultado é {resultado}')
        historico.append(f"{n1} * {n2} = {resultado}")
    
    elif opçao == 4:
        n1 = float (input('Digite um numero: '))
        n2 = float(input('Digite um numero: '))
        if n2 != 0:
            resultado = n1 / n2
            print(f'O resultado é {resultado}')
            historico.append(f"{n1} / {n2} = {resultado}")
        else:
            print('Não é possivel dividir por zero')
            historico.append(f"{n1} / {n2} = ERRO! (divisão por zero)")

    elif opçao == 5:
        base = float (input('Digite a base da potência: '))
        expoente = float(input('Digite o expoente da potência: '))
        resultado = base**expoente
        print(resultado)
        historico.append(f"{base} ** {expoente} = {resultado}")

    elif opçao == 6:
        radicando = int(input('Digite um número: '))
        indice = int(input('Digite o indice: '))
        raiz = radicando ** (1/indice)
        print(raiz)
        historico.append(f"{radicando} ** {indice} = {raiz}")
        

    elif opçao == 7:
        valor = int(input('Digite o valor:'))
        porcentagem = int(input('Digite a porcentagem:'))
        resultado = ((valor * porcentagem)/100)
        print(resultado)
        historico.append(f"{valor} + {porcentagem} = {resultado}")

    if opçao == 8:
        print(historico)
            
    

    if opçao == 10:
        menu = "s"
    
    

    if opçao < 0 or opçao >= 11:
        print('Operação Invalida!')
