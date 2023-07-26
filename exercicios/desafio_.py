def main():
    n = int(input())
    cupom = int(input())
    total = 0
    
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor

    if cupom == 10:
      desconto = total * 0.1
    elif cupom == 20:
      desconto = total * 0.2
    else:
      desconto = 0.0

    valor_com_desconto = total - desconto
    
    print(f"Valor total: {valor_com_desconto:.2f}")

if __name__ == "__main__":
    main()
