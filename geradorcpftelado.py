import tkinter as tk
import random

#função para gerar cpf

def gerador_cpf():
    nove_digitos = ''.join(str(random.randint(0, 9)) for _ in range(9))

    contador_regressivo01 = 10
    resultado_digito_01 = 0
    for digito in nove_digitos:
        resultado_digito_01 += int(digito) * contador_regressivo01
        contador_regressivo01 -= 1
    
    digito_01 = (resultado_digito_01 * 10) % 11
    digito_01 = digito_01 if digito_01 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_01)
    contador_regressivo02 = 11
    resultado_digito_02 = 0
    for digito in dez_digitos:
        resultado_digito_02 += int(digito) * contador_regressivo02
        contador_regressivo02 -= 1
    digito_02 = (resultado_digito_02 * 10) % 11
    digito_02 = digito_02 if digito_02 <= 9 else 0

    cpf_completo = nove_digitos + str(digito_01) + str(digito_02)
    return cpf_completo

#criando interface gráfica

def atualizar_cpf_label():
    cpf_gerado = gerador_cpf()
    cpf_label.config(text=f'CPF Gerado: {cpf_gerado}')

root = tk.Tk()
root.title("Super Gerador de CPF")

cpf_label = tk.Label(root, text='CPF Gerado: ')

botao_gerador = tk.Button(root, text= 'Gere seu CPF(grátis)', command=atualizar_cpf_label)

cpf_label.pack()
botao_gerador.pack()

root.mainloop()