def valorPagamento(valor, dias):

    if (dias == 0):

        return valor
    
    else:

        novo_valor = (1.03 * valor) + (0.01 * dias)

        return novo_valor


valor = float(input("Valor do pagamento (fim = 0): "))

count = 0

soma = 0

while(valor > 0):

    dias = int(input("Dias de atraso: "))

    count += 1
    
    prestacao = valorPagamento(valor, dias)
    
    soma += prestacao

    print("Valor a ser pago: ", prestacao)

    

    valor = float(input("Valor do pagamento (fim = 0): "))

print("Relatório do dia:")
print(count,"prestações\nSoma das prestações:",soma)
    

    