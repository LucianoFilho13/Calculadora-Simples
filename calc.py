import math #Importações responsável em calcular raiz quadrada

decision = str(input("Deseja iniciar um calculo ? [Y/N] "))

#While = Enquanto
while decision == 'y' or decision == 'Y':
    print("Número 1: Adição")
    print("Número 2: Subtração")
    print("Número 3: Multiplicação")
    print("Número 4: Divisão")
    print("Número 5: Raiz Quadrada")

    choose = int(input("Digite um dos valores acima: "))

    if (choose == 1 or choose == 2 or choose == 3 or choose == 4 or choose == 5):
        if (choose == 1):
            print("Equação escolhida: Adição!")
        if (choose == 2): 
            print("Equação escolhida: Subtração!")
        if (choose == 3):
            print("Equação escolhida: Multiplicação!")
        if (choose == 4):
            print("Equação escolhida: Divisão!")

        if (choose == 5):
            print("Equação escolhida: Divisão!")
            num = float(input("Digite o número desejado:\n"))
            raiz = math.sqrt(num)
            print(f'\nA raiz quadrada de {num} é {raiz}\n')
        else:
            amountNumber = int(input("Quantos números estará na equação ? O número máximo é 4! "))
        

            if (amountNumber <= 1):
                print("Quantidade Invalida!")
            if (amountNumber == 2):
                num1 = float(input("Digite o Primeiro Número: "))
                num2 = float(input("Digite o Segundo Número: "))
            if (amountNumber == 3):
                num1 = float(input("Digite o Primeiro Número: "))
                num2 = float(input("Digite o Segundo Número: "))
                num3 = float(input("Digite o Terceiro Número: "))
            if (amountNumber == 4):
                num1 = float(input("Digite o Primeiro Número: "))
                num2 = float(input("Digite o Segundo Número: "))
                num3 = float(input("Digite o Terceiro Número: "))
                num4 = float(input("Digite o Quarto Número: "))
            if (amountNumber > 4):
                print("Quantidade Invalida!")
            

            if (choose == 1 and amountNumber == 2):
                print(num1 + num2)
            if (choose == 1 and amountNumber == 3):
                print(num1 + num2 + num3)
            if (choose == 1 and amountNumber == 4):
                print(num1 + num2 + num3 + num4)

            if (choose == 2 and amountNumber == 2): 
                print(num1 - num2)
            if (choose == 2 and amountNumber == 3): 
                print(num1 - num2 - num3)
            if (choose == 2 and amountNumber == 4): 
                print(num1 - num2 - num3 - num4)

            if (choose == 3 and amountNumber == 2):
                print(num1 * num2)
            if (choose == 3 and amountNumber == 3):
                print(num1 * num2 * num3)
            if (choose == 3 and amountNumber == 4):
                print(num1 * num2 * num3 * num4)

            if (choose == 4 and amountNumber == 2):
                print(num1 / num2)

            if (choose == 4 and amountNumber >= 3):
                print("Não é possivel realizar essa equação!")


    else:
        print("Valor inválido")

    decision = str(input("Deseja fazer um calculo ? [Y/N] "))

if (decision == 'n' or decision == 'N'):
    print("Ok, agradeço por me chamar!")

if (decision != 'n' or decision != 'N' or decision != 'y' or decision != 'Y'):
    print("Resposta Inválida!")