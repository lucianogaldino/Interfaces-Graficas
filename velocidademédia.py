from tkinter import*

janela = Tk()

def clicar():#definição da relação do botão com o label
    if(str(txt1.get())) == '?':
        ds = float(txt2.get())
        dt = float(txt3.get())
        vm = ds / dt
        lb5['text'] = vm
    elif (str(txt2.get())) == '?':
        vm = float(txt1.get())
        dt = float(txt3.get())
        ds = vm * dt
        lb5['text'] = ds
    elif (str(txt3.get())) == '?':
        vm = float(txt1.get())
        ds = float(txt2.get())
        dt = ds / vm
        lb5['text'] = dt
    else:
        lb5["text"] = 'Erro de digitação!'

janela.title("CÁLCULOS ENVOLVENDO VELOCIDADE MÉDIA")
janela["bg"] ="blue" #bg é simplificação de blackground

# criando caixa de texto
txt1 = Entry(janela)
txt1.place(x=330, y=80)

txt2 = Entry(janela)
txt2.place(x=330, y=120)

txt3 = Entry(janela)
txt3.place(x=330, y=160)

#criando labelS
lb1 = Label(janela, text='ORIENTAÇÕES:\n'
                        '1) Utilizar os valores com unidades de medidas no SI.\n'
                        '2) Colocar ponto de interrogação (?) na grandeza que se deseja calcular.')
lb1.place(x=80, y=20)#posicionamento

lb2 = Label(janela, text='DIGITE A VELOCIDADE MÉDIA (m/s)')
lb2.place(x=80, y=80)#posicionamento

lb3 = Label(janela, text='DIGITE A VARIAÇÃO DA POSIÇÃO (m)')
lb3.place(x=80, y=120)#posicionamento

lb4 = Label(janela, text='DIGITE A VARIAÇÃO DO TEMPO (s)')
lb4.place(x=80, y=160)#posicionamento

lb5 = Label(janela, text='RESULTADO')
lb5.place(x=330, y=200)#posicionamento

#criando botão
bt = Button(janela, width=10, text='CALCULAR', command=clicar)
bt.place(x=180, y=200)


janela.geometry('550x250+200+100') #Janela tem largura de 600, altura de 300 margem direita 200 e margem esquerda 100


janela.mainloop()
