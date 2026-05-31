
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math 

#### CALCULADORA UNICA DE MEDIDA #####
def calculoDentesMedida():

    def calcular_medida_sobre_dentes():
        modulo = float(entry_modulo.get())
        angulo_pressao = float(entry_angulo_pressao.get())
        numero_dentes = int(entry_numero_dentes.get())
        
        angulo_pressao_rad = math.radians(angulo_pressao)
        c1 = modulo * math.cos(math.radians(angulo_pressao))
        c2 = (math.pi * ((numero_dentes - 1) + 0.5)) + (angulo_pressao_rad * math.tan(angulo_pressao_rad))
        medida = c1 * c2
        
        resultado_textarea.delete(1.0, tk.END)
        resultado_textarea.insert(tk.END, f"A medida sobre dentes de {numero_dentes} dentes é: {medida:.2f} mm")

   
    root1 = tk.Tk()
    root1.title("Calculadora de Medida sobre Dentes")

    # Criando os widgets
    label_modulo = ttk.Label(root1, text="Módulo:")
    entry_modulo = ttk.Entry(root1)
    label_angulo_pressao = ttk.Label(root1, text="Ângulo de Pressão (graus):")
    entry_angulo_pressao = ttk.Entry(root1)
    label_numero_dentes = ttk.Label(root1, text="Número de Dentes:")
    entry_numero_dentes = ttk.Entry(root1)
    btn_calcular = ttk.Button(root1, text="Calcular", command=calcular_medida_sobre_dentes)
    resultado_textarea = tk.Text(root1, height=5, width=50)

    # Posicionando os widgets na janela
    label_modulo.grid(row=0, column=0, padx=5, pady=5, sticky="e")
    entry_modulo.grid(row=0, column=1, padx=5, pady=5, sticky="w")
    label_angulo_pressao.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    entry_angulo_pressao.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    label_numero_dentes.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    entry_numero_dentes.grid(row=2, column=1, padx=5, pady=5, sticky="w")
    btn_calcular.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    resultado_textarea.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    # Iniciando o loop principal da interface gráfica
    root1.mainloop()

##### CALCULADORA DE ENGRENAGENS #####

def abrir_calculadora():

    def calculosRetos():
        
        def verificarCampos2():
            if dentesEngr1.get() == '':
                messagebox.showinfo("Campo Vazio ou Inválido!", "Insira um valor para o campo de dentes!")  
            elif moduloEngr1.get() == '':
                messagebox.showinfo("Campo Vazio ou Inválido", "Insira um valor para o módulo!")
            elif dentesEngr2.get() == '':
                messagebox.showinfo("Campo Vazio ou Inválido!", "Insira um valor para o campo de dentes!")
            elif moduloEngr2.get() == '':
                messagebox.showinfo("Campo Vazio ou Inválido", "Insira um valor para o módulo!")
        
        verificarCampos2()
    
        z1 = float(dentesEngr1.get()) 
        m1 = float(moduloEngr1.get())  
        ah1  = float(heliceEngr1.get())
        
        z2 = float(dentesEngr2.get())  
        m2 = float(moduloEngr2.get())

        ah_rad = math.radians(ah1)
        resultado = 0

        # calculos com engrenagens de dentes retos
        if combo_var1.get() == 'Dentes Retos':
            
            calculo = combo_var2.get() 

            if calculo == 'Distância entre centros (C)':
                dp1 = m1 * z1
                dp2 = m2 * z2
                resultado = (dp1 + dp2) / 2

            elif calculo == 'Relação de transmissão (RT)':
                resultado = z2 / z1    

        else:
            # calculos com engrenagens de dentes helicoidais
    
            calculo = combo_var2.get() 

            if combo_var2.get() == 'Distância entre centros (c)':
                mA = m1 / math.cos(ah_rad)
                resultado = ((z1 + z2) / 2) * mA
            elif calculo == 'Relação de transmissão (rt)':
                resultado = z2 / z1

        textArea.delete(0, tk.END) 
        textArea.insert(tk.END, f"Resultado: {resultado:.2f} mm")



    ##### NOVA JANELA #####
    janela_calculadora = tk.Toplevel(window)
    janela_calculadora.title(f'Cálculo: {combo_var2.get()}')
    janela_calculadora.geometry("850x400")
    janela_calculadora.transient(window)
    
    
    texto = tk.Label(janela_calculadora, text=f'Preencha os campos abaixo para o\n{combo_var2.get()}')
    texto.grid(row=0, column=1, padx=10, pady=5)

    entry1Label = tk.Label(janela_calculadora, text='Nº de dentes da primeira engrenagem: ')
    entry1Label.grid(row=1, column=0, padx=10, pady=5)
    dentesEngr1 = tk.Entry(janela_calculadora)
    dentesEngr1.grid(row=2, column=0, padx=10, pady=5)
    
    entry2Label = tk.Label(janela_calculadora, text='Módulo da primeira engrenagem: ')
    entry2Label.grid(row=3, column=0, padx=10, pady=5)
    moduloEngr1 = tk.Entry(janela_calculadora)
    moduloEngr1.grid(row=4, column=0, padx=10, pady=5)

    entry3Label = tk.Label(janela_calculadora, text='Ângulo de pressão da primeira engrenagem: ')
    entry3Label.grid(row=5, column=0, padx=10, pady=5)
    pressaoEngr1 = tk.Entry(janela_calculadora)
    pressaoEngr1.grid(row=6, column=0, padx=10, pady=5)
    
    entry4Label = tk.Label(janela_calculadora, text='Ângulo de hélice da primeira engrenagem: ')
    entry4Label.grid(row=7, column=0, padx=10, pady=5)
    heliceEngr1 = tk.Entry(janela_calculadora)
    heliceEngr1.grid(row=8, column=0, padx=10, pady=5)

    entry5Label = tk.Label(janela_calculadora, text='Nº de dentes da segunda engrenagem: ')
    entry5Label.grid(row=1, column=2, padx=10, pady=5)
    dentesEngr2 = tk.Entry(janela_calculadora)
    dentesEngr2.grid(row=2, column=2, padx=10, pady=5)
    
    entry6Label = tk.Label(janela_calculadora, text='Módulo da segunda engrenagem: ')
    entry6Label.grid(row=3, column=2, padx=10, pady=5)
    moduloEngr2 = tk.Entry(janela_calculadora)
    moduloEngr2.grid(row=4, column=2, padx=10, pady=5)
    
    entry7Label = tk.Label(janela_calculadora, text='Ângulo de pressão da segunda engrenagem: ')
    entry7Label.grid(row=5, column=2, padx=10, pady=5)
    pressaoEngr2 = tk.Entry(janela_calculadora)
    pressaoEngr2.grid(row=6, column=2, padx=10, pady=5)
    
    entry8Label = tk.Label(janela_calculadora, text='Ângulo de hélice da segunda engrenagem: ')
    entry8Label.grid(row=7, column=2, padx=10, pady=5)
    heliceEngr2 = tk.Entry(janela_calculadora)
    heliceEngr2.grid(row=8, column=2, padx=10, pady=5)
    

    botao_calcular = ttk.Button(janela_calculadora, text="Calcular", command=calculosRetos)
    botao_calcular.grid(row=7, column=1, padx=10, pady=5)
    
    fonte = ('Helvetica', 12,'bold')
    ResultadoLabel = tk.Label(janela_calculadora, text='Resultado:')
    ResultadoLabel.grid(row=8, column=1, padx=10, pady=5)
    textArea = tk.Entry(janela_calculadora,font=fonte, justify='center')
    textArea.grid(row=10, column=1, padx=10, pady=5)

# verificar campos
def verificarCampos():
    # numero de dentes
    if entry6.get() == '':
        messagebox.showinfo("Campo Vazio ou Inválido", "Insira um número inteiro para os dentes!")
    # modulo
    elif entry3.get() == '':
        messagebox.showinfo("Campo Vazio ou Inválido", "Insira um valor decimal para o módulo!")
    # angulo helice
    elif entry5.get() == '':
        messagebox.showinfo("Campo Vazio", "Insira um valor para o ângulo de hélice!")
    # angulo pressao
    elif entry4.get() == '':
        messagebox.showinfo("Campo Vazio", "Insira um valor para o ângulo de pressão!")
 
def exibirCalculo():
    calculo = combo_var2.get()
    entry7.delete(0, tk.END)  
    entry7.insert(tk.END, calculo)  


def verificarCalculo(event):
    engrenagem = combo_var1.get()
    valor = combo_var2.get()
    if engrenagem =='Dentes Retos':
        if valor == 'Distância entre centros (C)' or valor == 'Relação de transmissão (RT)':
            abrir_calculadora()
        elif valor == 'Medida sobre dentes (M)':
            calculoDentesMedida()
    else:
        if valor == 'Distância entre centros (c)' or valor == 'Relação de transmissão (rt)':
            abrir_calculadora()

def botaoClique():
    verificarCampos()
    entry0.delete("1.0",tk.END)
    resultado = 0
    
    # inputs 
    modulo = float(entry3.get())
    numeroDentes = float(entry6.get())
    anguloHelice = float(entry5.get())
    anguloPressao = float(entry4.get())
    
    angulo_pressao_rad = math.radians(anguloPressao)
    angulo_helice_rad =  math.radians(anguloHelice)
    
    if combo_var1.get() == 'Dentes Retos':
    
        # calculos retos
        
        p = modulo * math.pi
        dp = modulo * numeroDentes
        alturaDente = 2.2 * modulo
        a = modulo
        alturaPe = 1.2 * modulo
        folga = 0.2 * modulo
        vaoDentesdp = (math.pi * 2) / 2
        espessuraDp = (math.pi * modulo) / 2

        if combo_var2.get() == 'Espessura no DP (T)':
            resultado = espessuraDp
        elif combo_var2.get() == 'Diâmetro Primitivo (DP)':
            resultado = dp
        elif combo_var2.get() == 'Passo (P)':
            resultado = p
        elif combo_var2.get() == 'Diâmetro de Base (DB)':
            resultado = dp * math.cos(angulo_pressao_rad)
        elif combo_var2.get() == "Vão entre dentes no dp (TS)":
            resultado = vaoDentesdp
        elif combo_var2.get() == "Altura do dente (H)":
            resultado = alturaDente
        elif combo_var2.get() == "Altura comum do dente (H´)":
            resultado = 2 * modulo
        elif combo_var2.get() == "Diâmetro externo (DE)":  
            resultado = modulo * (numeroDentes + 2)
        elif combo_var2.get() == "Diâmetro interno (DI)":  
            resultado = modulo * (numeroDentes - 2.4)
        elif combo_var2.get() == 'Altura da cabeça (A)':
            resultado = a
        elif combo_var2.get() == 'Altura do Pé (D)':
            resultado = alturaPe
        elif combo_var2.get() == "Folga da Cabeça (F)":
            resultado = folga
       

    else:

         # calculos helicoidais

        p = modulo * math.pi
        passoAparente = ( modulo * math.pi / math.cos(angulo_helice_rad))
        espessuraNormal = (math.pi * modulo) / 2
        espessuraFrontal = passoAparente / 2 
        moduloAparente = modulo / math.cos(angulo_helice_rad)
        diametroPrimitivo = moduloAparente * numeroDentes
        alturadoDente = 2.2 * modulo
        alturaCabeca = modulo
        alturaPe = 1.2 * modulo
        folga = 0.2 * modulo
        diametroBase = (diametroPrimitivo * math.cos(angulo_pressao_rad))

        if combo_var2.get() == 'Espessura Normal (t)':
            resultado = espessuraNormal
        elif combo_var2.get() == 'Espessura Frontal (ta)':
            resultado = espessuraFrontal
        elif combo_var2.get() == 'Passo normal (p)':
            resultado = p
        elif combo_var2.get() == 'Passo aparente (pa)':
            resultado = passoAparente
        elif combo_var2.get() == 'Módulo aparente (ma)':
            resultado = moduloAparente
        elif combo_var2.get() == 'Altura do dente (h)':
            resultado = alturadoDente
        elif combo_var2.get() == 'Altura da cabeça (a)':
            resultado = alturaCabeca
        elif combo_var2.get() == 'Altura do pé (d)':
            resultado = alturaPe
        elif combo_var2.get() == 'Folga da cabeça (f)':
            resultado = folga
        elif combo_var2.get() == 'Passo helicoidal (ph)':
            resultado =   (math.pi * modulo) / math.sin(angulo_helice_rad)
        elif combo_var2.get() =="Diâmetro Primitivo (dp)":
            resultado = diametroPrimitivo
        elif combo_var2.get() == 'Diâmetro interno (di)':
            resultado = diametroPrimitivo - 2.4 * modulo
        elif combo_var2.get() == 'Diâmetro externo (de)':
            resultado = diametroPrimitivo + 2 * modulo
        elif combo_var2.get() == 'Diâmetro base (db)':
            resultado = diametroBase
        elif combo_var2.get() == 'Ângulo de pressão apar.':
            resultado = math.degrees(math.atan(math.tan(angulo_pressao_rad) /math.cos(angulo_helice_rad)))
        elif combo_var2.get() == 'Medida sobre dentes (m)':
            messagebox.showinfo('Em andamento...', 'Calculo não disponível!')

    exibirCalculo()
    entry0.insert("1.0", f'\n{resultado:.2f} mm' ,'center')


def atualizar_opcoes_combobox2(event=None):
    valor_selecionado = combo_var1.get()
    
    # Limpar as opções do segundo combobox
    combo_var2.set("")  # Limpar a seleção atual
    combo_box2['values'] = []  # Limpar as opções atuais


    if valor_selecionado == "Dentes Retos": # opcoes de calculos retos
        novas_opcoes = ["Passo (P)","Espessura no DP (T)","Vão entre dentes no dp (TS)","Diâmetro Primitivo (DP)",
                        "Distância entre centros (C)","Altura do dente (H)","Altura da cabeça (A)",
                        "Altura do Pé (D)","Folga da Cabeça (F)","Altura comum do dente (H´)",
                        "Diâmetro externo (DE)","Diâmetro interno (DI)","Diâmetro de Base (DB)",
                        'Relação de transmissão (RT)','Medida sobre dentes (M)']
    

    elif valor_selecionado == "Dentes Helicoidais": # opcoes de calculos helicoidais
        novas_opcoes = ["Espessura Normal (t)", 'Espessura Frontal (ta)',"Passo normal (p)","Passo aparente (pa)",
                        "Diâmetro Primitivo (dp)", 'Módulo aparente (ma)','Altura do dente (h)',
                        'Altura da cabeça (a)', 'Altura do pé (d)', 'Folga da cabeça (f)','Passo helicoidal (ph)',
                        'Distância entre centros (c)', 'Relação de transmissão (rt)','Diâmetro interno (di)',
                        'Diâmetro externo (de)', 'Diâmetro base (db)','Ângulo de pressão apar.','Medida sobre dentes (m)']

    else:
        novas_opcoes = [] 
    
    
    combo_box2['values'] = novas_opcoes
    return valor_selecionado


#### JANELA PRINCIPAL ####
window = Tk()
combo_var1 = tk.StringVar() 
combo_var2 = tk.StringVar() 

window.geometry("882x555")
window.configure(bg = "#ffffff")
window.title('Cálculo de Engrenagens')
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 555,
    width = 882,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    441.0, 277.5,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    661.5, 350.0,
    image = entry0_img)



entry0 = Text(
    bd = 0,
    bg = "#ededed",
    highlightthickness = 0,
    font=("Helvetica", 50, "bold"))

entry0.tag_configure('center', justify='center')

entry0.place(
    x = 487, y = 210,
    width = 349,
    height = 278)

style = ttk.Style()
style.theme_use('default')  # Use o tema padrão 

opcoes1 = ["Dentes Retos","Dentes Helicoidais"]

# primeiro combobox 
combo_box1 = ttk.Combobox(window, textvariable=combo_var1, values=opcoes1, state='readonly')
combo_box1.place(x=75, y=80, width=268, height=35)
combo_box1.bind("<<ComboboxSelected>>", atualizar_opcoes_combobox2)  # Atualizar o segundo combobox quando a seleção do primeiro combobox mudar

# segundo combobox
combo_box2 = ttk.Combobox(window, textvariable=combo_var2,state='readonly')
combo_box2.place(x=75, y=444, width=268, height=44)
combo_box2.bind("<<ComboboxSelected>>", verificarCalculo)


# numero de dentes

entry6_img = PhotoImage(file = f"img_textBox6.png")
entry6_bg = canvas.create_image(
    209.0, 186.5,
    image = entry6_img)

entry6 = Entry(
    bd = 0,
    bg = "#ededed",
    highlightthickness = 0)

entry6.place(
    x = 75, y = 171,
    width = 268,
    height = 29)


# modulo
entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvas.create_image(
    209.0, 246.5,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#ededed",
    highlightthickness = 0)

entry3.place(
    x = 75, y = 231,
    width = 268,
    height = 29)


# angulo de helice
entry5_img = PhotoImage(file = f"img_textBox5.png")
entry5_bg = canvas.create_image(
    209.0, 306.5,
    image = entry5_img)

entry5 = Entry(
    bd = 0,
    bg = "#ededed",
    highlightthickness = 0)

entry5.place(
    x = 75, y = 291,
    width = 268,
    height = 29)

# angulo de pressao
entry4_img = PhotoImage(file = f"img_textBox4.png")
entry4_bg = canvas.create_image(
    209.0, 366.5,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#ededed",
    highlightthickness = 0)

entry4.place(
    x = 75, y = 351,
    width = 268,
    height = 29)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = botaoClique,
    relief = "flat")

b0.place(
    x = 133, y = 507,
    width = 151,
    height = 36)

# exibir qual o calculo
entry7_img = PhotoImage(file = f"img_textBox7.png")
entry7_bg = canvas.create_image(
    662.0, 520.5,
    image = entry7_img)

entry7 = Entry(
    bd = 0,
    bg = "#ededed",
    highlightthickness = 0,
    justify='center',
    font=("Helvetica", 10, "bold"))

entry7.place(
    x = 546, y = 505,
    width = 232,
    height = 29)

window.resizable(False, False)
window.mainloop()

