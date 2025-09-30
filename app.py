print("Bem vindo à calculadora básica")

while True:  # Loop principal para reiniciar a calculadora
    print("Digite dois numeros e escolha a operação (+, -, *, /)")

    #entrada
    while True: # laço infinito (true)
        try: # realiza uma tentativa
            num1 = float(input("Digite um numero: "))
            break # parar o laço
        except: #se houver alguma exceção (erro)
            print("Digite um numero válido. ")   

    while True:
        try:
            num2 = float(input("Digite outro numero: "))    
            break
        except:
            print("Digite um numero válido. ")

    while True:
        opr = input("Escolha operador: ") #string não precisa declarar
        if opr in ("+", "-", "*", "/"): # in vai verificar se dentro da variavel foi atribuido uma dessas strings
            break
        else: 
            print("Digite um operador válido. ")  
    
    resultado = None # variavel sem input não é obrigado a declarar tipo (reconhecimento automatico pro python)

    #processamento
    if opr == "+": # = atribuição // == comparação
        resultado = num1 + num2
    elif opr == "-": # if primeiro // elif para mais opçoes (2° para frente // else para ultima opção)
        resultado = num1 - num2
    elif opr == "*":
        resultado = num1 * num2
    elif opr == "/":
        if num2 != 0: #encadeamento de condição: uma uma condição dentro de outra. 
            resultado = num1 / num2
        else:
            print(" Não é possivel dividir por 0")  
            exit()

    # resultado        
    print(f"Resultado: {resultado}") # f de format (para mostrar o que tem dentro da variavel)

    saida = input("Deseja sair? S/N: ").upper() # metodo para deixar caracteres em maiusuculo.
    if saida == "S":
        print("Obrigado por usar a caulculadora do Fernando! ")
        break
    elif saida == "N":
        pass  # reinicia o programa automaticamente

