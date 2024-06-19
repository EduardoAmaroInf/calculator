from calculadora import Calculadora

def main():
    calc = Calculadora()

    # Inserir laço para ele repetir até o usuário decidir sair
    print("Calculadora Simples")
    print("===================")
    
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    
    operacao = input("Escolha a operação (+, -, *, /): ")
    
    if operacao == '+':
        resultado = calc.adicionar(a, b)
    elif operacao == '-':
        resultado = calc.subtrair(a, b)
    elif operacao == '*':
        resultado = calc.multiplicar(a, b)
    elif operacao == '/':
        resultado = calc.dividir(a, b)
    else:
        print("Operação inválida.")
        return

    print(f"O resultado de {a} {operacao} {b} é: {resultado}")

if __name__ == "__main__":
    main()
