def calcular():
    print("\nCalculadora Python no GitHub!")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    
    opcao = input("Escolha (1-4): ")
    num1 = float(input("Número 1: "))
    num2 = float(input("Número 2: "))
    
    if opcao == '1':
        print(f"Resultado: {num1 + num2}")
    elif opcao == '2':
        print(f"Resultado: {num1 - num2}")
    elif opcao == '3':
        print(f"Resultado: {num1 * num2}")
    elif opcao == '4':
        print(f"Resultado: {num1 / num2 if num2 != 0 else 'Erro!'}")
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    calcular()