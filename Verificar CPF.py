from tkinter import *
#Função Tratar cpf
def capitura(event=None):    
    x=in3_fr1.get().replace('.','').replace('-', '')[:11]
    y=''
    if event.keysym == "backspace": return
    for i in range(len(x)):
        if x[i] in '0123456789':
            if i in [2,5]:
                y+=x[i] + '.'
            elif i == 8:
                y+=x[i] + '-'
            else:
                y+=x[i]
    in3_fr1.delete(0, 'end')
    in3_fr1.insert(0, y)
#Função Tratar Data
def data(event=None):    
    x=in2_fr1.get().replace('/','')[:8]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if not x[i] in '0123456789': continue
        if i in [1,3]:
            y+=x[i] + '/'
        else:
            y+=x[i]
    in2_fr1.delete(0, 'end')
    in2_fr1.insert(0, y)
#Função Tratar 

#CRÉDITO ao JeanExtreme002. Resposta disponível em: https://pt.stackoverflow.com/questions/492705/criando-um-entry-formatado-para-cpf-em-python-tkinter#:~:text=Para%20formatar%20o%20CPF%20enquanto,e%20a%20fun%C3%A7%C3%A3o%20de%20formata%C3%A7%C3%A3o.
#Criando Janela e Frames
root = Tk()
root.title('Cadastro')
fr1 = LabelFrame(root, padx=10, pady=10, bg='#49A', text='Dados Pessoais', font='Arial 25', borderwidth=1, relief="sunken")
fr2 = LabelFrame(root, padx=10, pady=10, bg='#49A', text='Endereço', font='Arial 25')
fr3 = LabelFrame(root, padx=10, pady=10, bg='#49A', font='Arial 25')
root.configure(bg='#49A')
#Configuração da Janela:
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
#Nomes com a primeira letra maiuscula
var =StringVar()
def caps(*args):
    var.set(var.get().title())
var.trace("w", caps)
#Label do 1º Frame:
lb1_fr1 = Label(fr1, text='Nome:', font='Arial 25', padx=10, pady=10, bg='#49A')
lb2_fr1 = Label(fr1, text='Data Nasc.:', font='Arial 25', padx=10, pady=10, bg='#49A')
lb3_fr1 = Label(fr1, text='CPF:', font='Arial 25', padx=10, pady=10, bg='#49A')
lb4_fr1 = Label(fr1, text='Telefone:', font='Arial 25', padx=10, pady=10, bg='#49A')
#Entry do 1º Frame:
in1_fr1 = Entry(fr1, font='Arial 25', textvariable=var)
in2_fr1 = Entry(fr1, font='Arial 25')
in2_fr1.insert(0, 'DD/MM/AA')
in2_fr1.bind("<KeyRelease>", data)


in3_fr1 = Entry(fr1, font='Arial 25')
in3_fr1.bind("<KeyRelease>", capitura)
in4_fr1 = Entry(fr1, font='Arial 25')
#Pack
fr1.grid(sticky=NSEW)
#Posição dos Label do 1º Frame:
lb1_fr1.grid(row=0, column=0, sticky=E)
lb2_fr1.grid(row=1, column=0, sticky=E)
lb3_fr1.grid(row=2, column=0, sticky=E)
lb4_fr1.grid(row=3, column=0, sticky=E)
#Posição dos Entry do 1º Frame:
in1_fr1.grid(row=0, column=1, columnspan= 2, sticky=EW)
in2_fr1.grid(row=1, column=1, sticky=E)
in3_fr1.grid(row=2, column=1, sticky=E)
in4_fr1.grid(row=3, column=1, sticky=E)
#Label do 2º Frame:
lb1_fr2 = Label(fr2, text='Rua:', font='Arial 25', padx=15, pady=10, bg='#49A')
lb2_fr2 = Label(fr2, text='Bairro:', font='Arial 25', padx=15, pady=10, bg='#49A')
lb3_fr2 = Label(fr2, text='Cidade:', font='Arial 25', padx=15, pady=10, bg='#49A')
lb4_fr2 = Label(fr2, text='Nº:', font='Arial 25', padx=15, pady=10, bg='#49A')
lb5_fr2 = Label(fr2, text='UF:', font='Arial 25', padx=15, pady=10, bg='#49A')
#Entry do 2º Frame:
in1_fr2 = Entry(fr2, font='Arial 25')
in2_fr2 = Entry(fr2, font='Arial 25')
in3_fr2 = Entry(fr2, font='Arial 25')
in4_fr2 = Entry(fr2, font='Arial 25')
in5_fr2 = Entry(fr2, font='Arial 25')
#Pack
fr2.grid(sticky=NSEW)
#Posição dos Label do 2º Frame:
lb1_fr2.grid(row=0, column=0, sticky=E)
lb2_fr2.grid(row=1, column=0, sticky=E)
lb3_fr2.grid(row=1, column=2, sticky=E)
lb4_fr2.grid(row=0, column=4, sticky=E)
lb5_fr2.grid(row=1, column=4, sticky=E)
#Posição dos Entry do 2º Frame:
in1_fr2.grid(row=0, column=1, columnspan= 3, sticky=EW)
in2_fr2.grid(row=1, column=1, sticky=EW)
in3_fr2.grid(row=1, column=3, sticky=EW)
in4_fr2.grid(row=0, column=5, sticky=EW)
in5_fr2.grid(row=1, column=5, sticky=EW)
#Criando dois buttons no 3º Fr
bt0_fr3 = Button(fr3, text='Gravar Dados', font='Arial 25',bg='green')
bt1_fr3 = Button(fr3, text='Listar Dados', font='Arial 25',bg='green')
bt2_fr3 = Button(fr3, text='0', font='Arial 25',bg='green', command=lambda: entrada('0'))
#Pack
fr3.grid(sticky=NSEW)
#Posição os buttons no 3º Frame:
bt0_fr3.grid(row=0, column=0, padx=10, pady=10, sticky=W)
bt1_fr3.grid(row=0, column=1, padx=10, pady=10, sticky=W)
bt2_fr3.grid(row=0, column=2, padx=10, pady=10, sticky=W)
#Configuração da Janela do 1º Frame:
#lb
lb1_fr1.grid_rowconfigure(0, weight=1)
lb1_fr1.grid_columnconfigure(0, weight=1)
lb2_fr1.grid_rowconfigure(1, weight=1)
lb2_fr1.grid_columnconfigure(0, weight=1)
lb3_fr1.grid_rowconfigure(2, weight=1)
lb3_fr1.grid_columnconfigure(0, weight=1)
lb4_fr1.grid_rowconfigure(3, weight=1)
lb4_fr1.grid_columnconfigure(0, weight=1)
#in
in1_fr1.grid_rowconfigure(0, weight=1)
in1_fr1.grid_columnconfigure(1, weight=1)
in2_fr1.grid_rowconfigure(1, weight=1)
in2_fr1.grid_columnconfigure(1, weight=1)
in3_fr1.grid_rowconfigure(2, weight=1)
in3_fr1.grid_columnconfigure(1, weight=1)
in4_fr1.grid_rowconfigure(3, weight=1)
in4_fr1.grid_columnconfigure(1, weight=1)
#Configuração da Janela do 2º Frame:
#lb
lb1_fr2.grid_rowconfigure(0, weight=1)
lb1_fr2.grid_columnconfigure(0, weight=1)
lb2_fr2.grid_rowconfigure(1, weight=1)
lb2_fr2.grid_columnconfigure(0, weight=1)
lb3_fr2.grid_rowconfigure(1, weight=1)
lb3_fr2.grid_columnconfigure(3, weight=1)
lb4_fr2.grid_rowconfigure(0, weight=1)
lb4_fr2.grid_columnconfigure(5, weight=1)
lb5_fr2.grid_rowconfigure(1, weight=1)
lb5_fr2.grid_columnconfigure(5, weight=1)
#in
in1_fr2.grid_rowconfigure(0, weight=1)
in1_fr2.grid_columnconfigure(1, weight=1)
in2_fr2.grid_rowconfigure(1, weight=1)
in2_fr2.grid_columnconfigure(1, weight=1)
in3_fr2.grid_rowconfigure(1, weight=1)
in3_fr2.grid_columnconfigure(4, weight=1)
in4_fr2.grid_rowconfigure(0, weight=1)
in4_fr2.grid_columnconfigure(6, weight=1)
in5_fr2.grid_rowconfigure(1, weight=1)
in5_fr2.grid_columnconfigure(6, weight=1)






#Loop
root.mainloop()
















