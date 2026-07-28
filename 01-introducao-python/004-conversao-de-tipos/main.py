valor_float = 28.0
print(type(valor_float))
valor_int = 28
print(type(valor_int))

valor_float_convertido = int(valor_float)
print('O valor float convertido é:',type(valor_float_convertido),valor_float_convertido)

valor_int_convertido = float(valor_int)
print('O valor int convertido é:',type(valor_int_convertido),valor_int_convertido)


'''
Conversão implícita, ou coerção, ocorre quando a conversão de tipo acontece durante a compilação ou em tempo de execução e é tratada automaticamente pelo Python.

a_int = 1
b_float = 1.0
c_sum = a_int + b_float
print(c_sum)
print(type(c_sum))
'''

'''
A conversão explícita de tipos, também chamada de type casting, ocorre quando você converte deliberadamente um valor de um tipo para outro. 
Essa abordagem dá controle direto sobre a conversão, pois você especifica explicitamente o tipo de destino no código. 
Ela é comum quando a conversão automática (implícita) do Python não atende ao que você precisa.

Por exemplo, se você quiser converter um número de ponto flutuante para inteiro, escreva:

int(3.14)  # Converts 3.14 to 3
'''