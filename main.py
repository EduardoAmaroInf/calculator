from calculadora import Calculadora

def main():
    calc = Calculadora()

    while True:
        print("\nCalculadora Simples")
        print("===================")
        
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        
        operacao = input("Escolha a operação (+, -, *, /) ou digite 's' para sair: ")

        if operacao == 's':
            print("Encerrando a calculadora.")
            break
        elif operacao in ['+', '-', '*', '/']:
            if operacao == '+':
                resultado = calc.adicionar(a, b)
            elif operacao == '-':
                resultado = calc.subtrair(a, b)
            elif operacao == '*':
                resultado = calc.multiplicar(a, b)
            elif operacao == '/':
                if b == 0:
                    print("Não é possível dividir por zero.")
                    continue  # Continue the loop without calculating if b is zero
                resultado = calc.dividir(a, b)
            
            print(f"O resultado de {a} {operacao} {b} é: {resultado}")
        else:
            print("Operação inválida. Por favor, escolha uma operação válida.")

if __name__ == "__main__":
    main()
