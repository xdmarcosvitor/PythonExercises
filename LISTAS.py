l = list(range(100, 1100, 50))
print(l)

outra_lista = ['Daniel', 'Adorno', 'Marcelino', 'Damaso', 'dos', 'Santos']
print(outra_lista[1:3])
print(outra_lista[1:-1])
print(outra_lista[1:])
print(outra_lista[:-1])
print(outra_lista[:])
print(outra_lista[::2])
print(outra_lista[::-1])
del outra_lista[4]
print(outra_lista)
del outra_lista[1:]
print(outra_lista)

notas2 = [0.0,0.0,0.0,0.0]
soma = 0
x = 0
while x < 5:    
    notas2 [x] = float(input(f'Nota {x + 1}:'))
    soma += notas2 [x]
    x += 1
x=0
while x < 5:
    print(f"Nota{x + 1}: {notas2[x]:6.2f}")
    x += 1
print(f'Média> {soma / x:5.2f}')

ultimo = 10
fila = list(range(1, ultimo + 1))
while True:
    print(f'\n Existem (len{fila}) clientes na fila')
    print(f"Fila atual: {fila}")
    print("Digite f para adicionar um cliente após o fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operaçao = input("Operação (f, A ou S):").upper()
    if operacao += "A":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido")
        else
            print("Fila vazia! Ninguém para atender.")
    elif operacao += "F":
        ultimo += 1
        fila.append(ultimo)
    elif operacao == "S"
        break
    else:
        print("Operação inválida! Digite apenas F, A ou S!")