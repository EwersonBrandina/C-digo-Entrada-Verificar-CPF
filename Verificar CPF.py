from tkinter import *
#MODELO CRIADO POR BRENO
root = Tk()
altura = root.winfo_screenheight()
largura = root.winfo_screenwidth()
root.geometry('590x470') # declara o tamanho da jenela (400x300) tamanho inicial/ +100 +100 lugar onde ela vai abrir
root.config(background='#fff') #background color
#root.grid_rowconfigure(0, weight=1)
#root.grid_columnconfigure(0, weight=1)
#Funções
def deposito(event=None):
    x = in0_fr4_1.get().replace(',', '.')
    y = ''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            y += x[i]
        elif x[i] in '.':
            y += x[i]
        else:
            y += ''
    if y.count('.') > 1:
        y=y[:-1]
    #y=float(y)
    #y=round(y)
    #y=str(y)
    in0_fr4_1.delete(0, 'end')
    in0_fr4_1.insert(0, y)
def saque(event=None):
    x = in0_fr4_2.get().replace(',', '.')
    y = ''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            y += x[i]
        elif x[i] in '.':
            y += x[i]
        else:
            y += ''
    if y.count('.') > 1:
        y=y[:-1]
    #y=float(y)
    #y=round(y)
    #y=str(y)
    in0_fr4_2.delete(0, 'end')
    in0_fr4_2.insert(0, y)
def transferencia(event=None):
    x = in0_fr4_3.get().replace(',', '.')
    y = ''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            y += x[i]
        elif x[i] in '.':
            y += x[i]
        else:
            y += ''
    if y.count('.') > 1:
        y=y[:-1]
    #y=float(y)
    #y=round(y)
    #y=str(y)
    in0_fr4_3.delete(0, 'end')
    in0_fr4_3.insert(0, y)
def extrato(event=None):
    x = in0_fr4_4.get().replace('/', '').replace('--','')[:16]
    y = ''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if not x[i] in '0123456789': continue
        if i in [1, 3, 9, 11]:
            y += x[i] + '/'
        elif i in [7]:
            y += x[i] + '--'
        else:
            y += x[i]
    in0_fr4_4.delete(0, 'end')
    in0_fr4_4.insert(0, y)
#NSEW
#-------------------------- Functions --------------------------#

#Aqui ficaram as funções do projeto

#-------------------------- Frame 0 / Widgets --------------------------#

#frX = LabelFrame(root, background='#fff', text='text', fg="gray", font='Georgia 15')
# X é o numero a ser substiuido pelo numero da sua flame

#lb0_frX = Label(frX, text="text", font='Georgia 15')
#Label padronizado
#bt0_frX = Button(frX, text="text", font='Georgia 15')
#Botão padronizado
#in0_frX = Entry(frX, font='Georgia 15')
#Entrada de dados (input) padronizado

#-------------------------- Frame 1 / Apresentar --------------------------#

#frX.grid()
#grid / para mostrar o flame
#lb0_frX.grid()
#grid / para mostrar o Label
#in0_frX.grid()
#grid / para mostrar a entrada de dados

#-------------------------- Mostrar tela --------------------------#

#root.mainloop()

#INÍCIO DO CÓDIGO

#Frame 0 - Gustavo

fr0 = LabelFrame ()

lb0_fr0 = Label(fr0, text='Seja Muito Bem-Vindo', font='Arial 30').grid(row=0,column=0, sticky=E,padx=50)
bt0_fr0 = Button(fr0, text='Funcionário', font='Arial 25', command= lambda: [fr0.grid_remove(), fr1.grid(row=0, column=0)]).grid(row=1, column=0, sticky=W, padx=20)
bt1_fr0 = Button(fr0, text='Usuario', font='Arial 25', command= lambda: [fr0.grid_remove(), fr3.grid(row=0, column=0)]).grid(row=1, column=0, sticky=E, padx=50)

fr0.grid(row=0, column=0, sticky=NSEW)
#Frame 1 - Samuel

#criar janela

fr1 = LabelFrame(root)

#criar os widgets

#---Frame 1---
lb0_fr1 = Label(fr1, text='Login do Funcionário', font='Arial 22').grid(row=0,column=1,sticky=W,padx=150)
lb1_fr1 = Label(fr1, text='Usuário:', font="Arial 20").grid(row=1, column=1,sticky=W, padx=5)
lb2_fr1 = Label(fr1, text='Senha:', font="Arial 20",width=7).grid(row=2, column=1,sticky=W, padx=5)

#--Entrada ---
int0_fr1 = Entry(fr1, font='Arial 18', width=35).grid(row=1,column=1,sticky=W,padx=110)
int1_fr1 = Entry(fr1, font='Arial 18', width=35).grid(row=2,column=1,sticky=W,padx=110)
#--Button ---
tb0_fr1 = Button(fr1,text='Entrar', font="Arial 20",width=15,bg='black', fg='white').grid(row=4, column=1, sticky=W, padx=110)
tb1_fr1 = Button(fr1, text='Voltar', font="Arial 20",width=15,bg='black', fg='white', command= lambda: [fr1.grid_remove(),fr0.grid(row=0, column=0)]).grid(row=4, column=1, sticky=E,padx=100)

#---Configuração do Frame---
##fr1.grid()
#
##organizar os widgets
#
##--Entrada --
#
##---Butoon Função---
#
##executar a janel4

#Frame 2 - Breno

#-------------------------- Frame 2 --------------------------#

fr2 = LabelFrame(root, background='#fff', text='Dados Pessoais', fg="blue", font='Georgia 12')
#fr2.grid(row=0, padx= 15)

#Linha 1
lb0_fr2 = Label(fr2, text="Nome:", font='Georgia 10').grid(row=1, column=0)
in0_fr2 = Entry(fr2, fg='blue', font='Georgia 10').grid(row=1, column=1, columnspan=5, sticky=NSEW)

#Linha 2
lb1_fr2 = Label(fr2, text="CPF:", font='Georgia 10').grid(row=2, column=0)
in1_fr2 = Entry(fr2, fg='blue', font='Georgia 10').grid(row=2, column=1)

lb2_fr2 = Label(fr2, text="Data Nasc:", font='Georgia 10').grid(row=2, column=2)
in2_fr2 = Entry(fr2, fg='blue', font='Georgia 10', cursor="gobbler").grid(row=2, column=3)

lb3_fr2 = Label(fr2, text="Telefone:", font='Georgia 10').grid(row=2, column=4)
in3_fr2 = Entry(fr2, fg='blue', font='Georgia 10').grid(row=2, column=5)

#Linha 3
lb4_fr2 = Label(fr2, text="Rua:", font='Georgia 10').grid(row=3, column=0)
lb4_fr2 = Entry(fr2, fg='blue', font='Georgia 10').grid(row=3, column=1, columnspan=3, sticky=NSEW)

lb5_fr2 = Label(fr2, text="  N° da casa:", font='Georgia 10').grid(row=3, column=4)
lb5_fr2 = Entry(fr2, fg='blue', font='Georgia 10').grid(row=3, column=5)

#linha 4
lb6_fr2 = Label(fr2, text="Bairro:", font='Georgia 10').grid(row=4, column=0,)
lb6_fr2 = Entry(fr2, fg='blue', font='Georgia 10').grid(row=4, column=1)

lb7_fr2 = Label(fr2, text="Cidade:", font='Georgia 10').grid(row=4, column=2)
lb7_fr2 = Entry(fr2, fg='blue', font='Georgia 10').grid(row=4, column=3)

lb8_fr2 = Label(fr2, text=" Estado:", font='Georgia 10').grid(row=4, column = 4)
lb8_fr2 = Entry(fr2, fg='blue', font='Georgia 10').grid(row=4, column=5)

#-------------------------- Frame 2.1 --------------------------#

fr2_1 = LabelFrame(root, background='#fff', text='Finalize seu cadastro', fg="blue", font='Georgia 12')
#fr2_1.grid(row=2, padx= 15, sticky=NSEW)

#Linha 8
bt0_fr1 = Button(fr2_1, text="Gravar Dados", font='Georfia 10').grid(row=8, column=0)
bt1_fr1 = Button(fr2_1, text="Listar Dados", font='Georfia 10').grid(row=8, column=1)


#Frame 3 - Felipe

#criando janela

fr3 = LabelFrame(root, text='Login / Cadastro', background='#10929c')
fr3_1 = LabelFrame(root, text='Cadastro', background='#10929c')

#criando widgets
lb0_fr3 = Label(fr3, text='Bem Vindo ao Dellux', font='Arial 20', background='#10929c', foreground='#f5f5f5')
lb1_fr3 = Label(fr3, text='O que deseja fazer?', font='Arial 20', background='#10929c', foreground='#f5f5f5')
lb2_fr3 = Label(fr3, text='Usuário:', font='Arial 20', background='#10929c', foreground='#f5f5f5')
lb3_fr3 = Label(fr3, text='Senha:', font='Arial 20', background='#10929c', foreground='#f5f5f5')
in0_fr3 = Entry(fr3,text='', font='Arial 20', background='#10929c')
in1_fr3 = Entry(fr3,text='', font='Arial 20', background='#10929c')

#widgets j2
lb4_fr3_1 = Label(fr3_1, text='Bem vindo a área de cadastro', font='Arial 20', background='#10929c', foreground='#f5f5f5')
lb5_fr3_1 = Label(fr3_1, text='Nome:', font='Arial 20', background='#10929c', foreground='#f5f5f5')
lb6_fr3_1 = Label(fr3_1, text='Data de Nasc:', font='Arial 20', background='#10929c', foreground='#f5f5f5')
lb7_fr3_1 = Label(fr3_1, text='CPF:', font='Arial 20', background='#10929c', foreground='#f5f5f5')
lb8_fr3_1 = Label(fr3_1, text='Telefone:', font='Arial 20', background='#10929c', foreground='#f5f5f5')
lb9_fr3_1 = Label(fr3_1, text='Endereço:', font='Arial 20', background='#10929c', foreground='#f5f5f5')
lb10_fr3_1 = Label(fr3_1, text='Cidade:', font='Arial 20', background='#10929c', foreground='#f5f5f5')
lb11_fr3_1 = Label(fr3_1, text='UF:', font='Arial 20', background='#10929c', foreground='#f5f5f5')
lb12_fr3_1 = Label(fr3_1, text='N°:', font='Arial 20', background='#10929c', foreground='#f5f5f5')
lb13_fr3_1 = Label(fr3_1, text='Email:', font='Arial 20', background='#10929c', foreground='#f5f5f5')
in2_fr3_1 =  Entry(fr3_1, text='', font='Arial 20', background='#10929c', foreground='#f5f5f5')
in3_fr3_1 =  Entry(fr3_1, text='', font='Arial 20', background='#10929c', foreground='#f5f5f5')
in4_fr3_1 =  Entry(fr3_1, text='', font='Arial 20', background='#10929c', foreground='#f5f5f5')
in5_fr3_1 =  Entry(fr3_1, text='', font='Arial 20', background='#10929c', foreground='#f5f5f5')
in6_fr3_1 =  Entry(fr3_1, text='', font='Arial 20', background='#10929c', foreground='#f5f5f5')
in7_fr3_1 =  Entry(fr3_1, text='', font='Arial 20', background='#10929c', foreground='#f5f5f5')
in8_fr3_1 =  Entry(fr3_1, text='', font='Arial 20', background='#10929c', foreground='#f5f5f5')
in9_fr3_1 =  Entry(fr3_1, text='', font='Arial 20', background='#10929c', foreground='#f5f5f5')
in10_fr3_1 =  Entry(fr3_1, text='', font='Arial 20', background='#10929c', foreground='#f5f5f5')

#botões
bt0_fr3 = Button(fr3, text='Login', font='Arial 20', background='#10929c', foreground='#f5f5f5', command= lambda:[fr3.grid_remove(), fr4.grid(row=0, column=0)])
bt1_fr3 = Button(fr3, text='Cadastro', font='Arial 20', background='#10929c', foreground='#f5f5f5', command= lambda:[fr3.grid_remove(), fr3_1.grid(row=0, column=0)] )
bt2_fr3_1 = Button(fr3_1, text='Salvar')
bt3_fr3_1 = Button(fr3_1, text='Voltar')

#frames
#fr3.grid()
#fr3_1.grid(padx=5)

#organizando widgets
lb0_fr3.grid(row=0, column=0, sticky=NSEW)
lb1_fr3.grid(row=1, column=0, sticky=NSEW)
lb2_fr3.grid(row=2, column=0, sticky=NE)
lb3_fr3.grid(row=3, column=0, sticky=NE)
in0_fr3.grid(row=2, column=1, sticky=NSEW)
in1_fr3.grid(row=3, column=1, sticky=NSEW)
bt0_fr3.grid(row=4, column=0, sticky=NSEW)
bt1_fr3.grid(row=4, column=1, sticky=NSEW)

#organizando widgets j2
lb4_fr3_1.grid(row=0, column=0)

#Nome
lb5_fr3_1.grid(row=1, column=0)
in2_fr3_1.grid(row=1, column=1, columnspan=4, sticky=NSEW)

#Data nasc
lb6_fr3_1.grid(row=2, column=0)
in3_fr3_1.grid(row=2, column=1) 

#CPF
lb7_fr3_1.grid(row=2, column=2)
in4_fr3_1.grid(row=2, column=3)  

#Telefone
lb8_fr3_1.grid(row=2, column=4)
in5_fr3_1.grid(row=2, column=5) 

#Endereço
lb9_fr3_1.grid(row=3, column=0)
in6_fr3_1.grid(row=3, column=1)

#Cidade
lb10_fr3_1.grid(row=4, column=0)
in7_fr3_1.grid(row=4, column=1) 

#UF
lb11_fr3_1.grid(row=4, column=2)
in8_fr3_1.grid(row=4, column=3) 

#N°
lb12_fr3_1.grid(row=4, column=4)
in9_fr3_1.grid(row=4, column=5)

#Email
lb13_fr3_1.grid(row=5, column=0)
in10_fr3_1.grid(row=5, column=1, columnspan=4, sticky=NSEW)


#Frame 4 - Ewerson
fr4 = LabelFrame(root, padx=10, pady=5, bg='#49A', text='Usuário', font='Arial 25', borderwidth=1, relief="sunken", width=5)
lb0_fr4 = Label(fr4, text='Ewerson Ribeiro Brandina', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=0, column=0 , sticky=W)
lb0_1_fr4 = Label(fr4, text='Número da Conta', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=0, column=2)
lb1_fr4 = Label(fr4, text='R$ 0.0', font='Arial 20',padx=5, pady=10, bg='#49A').grid(row=1, column=0, sticky=W)
bt2_fr4 = Button(fr4, text='Depósito', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4.grid_remove(), fr4_1.grid(row=0, column=1)]).grid(row=2, column=0, sticky=W)
bt3_fr4 = Button(fr4, text='Saque', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4.grid_remove(), fr4_2.grid(row=0, column=1)]).grid(row=3, column=0, sticky=W)
bt4_fr4 = Button(fr4, text='Transferência', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4.grid_remove(), fr4_3.grid(row=0, column=1)]).grid(row=4, column=0, sticky=W)
bt5_fr4 = Button(fr4, text='Extrato', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4.grid_remove(), fr4_4.grid(row=0, column=1)]).grid(row=5, column=0, sticky=W)
bt6_fr4 = Button(fr4, text='Pix', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=6, column=0, sticky=W)
bt7_fr4 = Button(fr4, text='Logout', font='Arial 20',padx=5, pady=0, bg='#49A',width=14).grid(row=7, column=2, sticky=E)
#fr4.grid(row=0, column=0, sticky=NSEW)
#Frame 4_1 - Ewerson
fr4_1 = LabelFrame(root, padx=10, pady=5, bg='#49A', text='Depósito', font='Arial 25', borderwidth=1, relief="sunken", width=5)
lb0_fr4_1 = Label(fr4_1, text='Valor a Ser Depositado', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=0, column=0 , sticky=W)
in0_fr4_1 = Entry(fr4_1, font='Arial 20', bg='#49A')
in0_fr4_1.bind("<KeyRelease>", deposito)
in0_fr4_1.grid(row=0, column=1)
in1_fr4_1 = Entry(fr4_1, font='Arial 20', bg='#49A').grid(row=1, column=1)
bt2_fr4_1 = Button(fr4_1, text='Confirmar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=2, column=0, columnspan=1, sticky=E)
lb3_fr4_1 = Label(fr4_1, text='Mensagem de Confirmação', font='Arial 20',padx=5, pady=0, bg='#49A',width=38).grid(row=3, column=0, columnspan=3, sticky=W)
bt4_fr4_1 = Button(fr4_1, text='Voltar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4_1.grid_remove(), fr4_2.grid_remove(), fr4_3.grid_remove(), fr4_4.grid_remove(),fr4.grid(row=0, column=0, sticky=NSEW)]).grid(row=4, column=0, sticky=E)
bt4_1_fr4_1 = Button(fr4_1, text='Logout', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=4, column=1, sticky=W)

#fr4_1.grid()
#Frame 4_2 - Ewerson
fr4_2 = LabelFrame(root, padx=10, pady=5, bg='#49A', text='Saque', font='Arial 25', borderwidth=1, relief="sunken", width=5)
lb0_fr4_2 = Label(fr4_2, text='Valor a Ser Sacado', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=0, column=0 , sticky=W)
in0_fr4_2 = Entry(fr4_2,font='Arial 20', bg='#49A')
in0_fr4_2.bind('<KeyRelease>', saque)
in0_fr4_2.grid(row=0, column=1)
in1_fr4_2 = Entry(fr4_2, font='Arial 20', bg='#49A').grid(row=1, column=1)
bt2_fr4_2 = Button(fr4_2, text='Confirmar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=2, column=0, columnspan=1, sticky=E)
lb3_fr4_2 = Label(fr4_2, text='Mensagem de Confirmação', font='Arial 20',padx=5, pady=0, bg='#49A',width=31).grid(row=3, column=0, columnspan=3, sticky=W)
bt4_fr4_2 = Button(fr4_2, text='Voltar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4_1.grid_remove(), fr4_2.grid_remove(), fr4_3.grid_remove(), fr4_4.grid_remove(),fr4.grid(row=0, column=0, sticky=NSEW)]).grid(row=4, column=0, sticky=E)
bt4_1_fr4_2 = Button(fr4_2, text='Logout', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=4, column=1, sticky=W)
#fr4_2.grid()
#Frame 4_3 - Ewerson
fr4_3 = LabelFrame(root, padx=10, pady=5, bg='#49A', text='Transferência', font='Arial 25', borderwidth=1, relief="sunken", width=5)
lb0_fr4_3 = Label(fr4_3, text='Valor a Ser Transferido', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=0, column=0 , sticky=W)
in0_fr4_3 = Entry(fr4_3,font='Arial 20', bg='#49A')
in0_fr4_3.bind('<KeyRelease>', transferencia)
in0_fr4_3.grid(row=0, column=1)
in1_fr4_3 = Entry(fr4_3, font='Arial 20', bg='#49A').grid(row=1, column=1)
bt2_fr4_3 = Button(fr4_3, text='Confirmar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=2, column=0, columnspan=1, sticky=E)
lb3_fr4_3 = Label(fr4_3, text='Mensagem de Confirmação', font='Arial 20',padx=5, pady=0, bg='#49A',width=31).grid(row=3, column=0, columnspan=3, sticky=W)
bt4_fr4_3 = Button(fr4_3, text='Voltar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4_1.grid_remove(), fr4_2.grid_remove(), fr4_3.grid_remove(), fr4_4.grid_remove(),fr4.grid(row=0, column=0, sticky=NSEW)]).grid(row=4, column=0, sticky=E)
bt4_1_fr4_3 = Button(fr4_3, text='Logout', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=4, column=1, sticky=W)
#fr4_3.grid()
#Frame 4_4 - Ewerson
fr4_4 = LabelFrame(root, padx=10, pady=5, bg='#49A', text='Extrato', font='Arial 25', borderwidth=1, relief="sunken", width=5)
lb0_fr4_4 = Label(fr4_4, text='PERIODO', font='Arial 20',padx=5, pady=0, bg='#49A').grid(row=0, column=0 , sticky=W)
in0_fr4_4 = Entry(fr4_4,font='Arial 20', bg='#49A')
in0_fr4_4.bind('<KeyRelease>', extrato)
in0_fr4_4.grid(row=0, column=1)
in1_fr4_4 = Entry(fr4_4, font='Arial 20', bg='#49A').grid(row=1, column=1)
bt2_fr4_4 = Button(fr4_4, text='Confirmar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=2, column=0, columnspan=1, sticky=E)
lb3_fr4_4 = Label(fr4_4, text='Mensagem de Confirmação', font='Arial 20',padx=5, pady=0, bg='#49A',width=27).grid(row=3, column=0, columnspan=3, sticky=W)
bt4_fr4_4 = Button(fr4_4, text='Voltar', font='Arial 20',padx=5, pady=0, bg='#49A',width=12, command= lambda: [fr4_1.grid_remove(), fr4_2.grid_remove(), fr4_3.grid_remove(), fr4_4.grid_remove(),fr4.grid(row=0, column=0, sticky=NSEW)]).grid(row=4, column=0, sticky=E)
bt4_1_fr4_4 = Button(fr4_4, text='Logout', font='Arial 20',padx=5, pady=0, bg='#49A',width=12).grid(row=4, column=1, sticky=W)
#fr4_4.grid()















#Looping para tudo
root.mainloop()
