from SpeckleAnaliser import SA
import tkinter  as tk
from tkinter import filedialog

global pasta_selecionada, salvar_pasta

def selecionar_pasta():
    global pasta_selecionada
    pasta_selecionada = filedialog.askdirectory(title="Selecione uma pasta")
    SA.set_folder(pasta_selecionada)

def executar():
    global pasta_selecionada        
    SA.Picture()
    label_prog.config(text="Concluído", fg="green")
    label_salvar.config(text= "", fg = color1)
    label_colorir.config(text= "", fg = color1)

def apenas_numeros(n):
    return n.isdigit() or n == ""

def colorir():
    if red.get() == '':
        RED = 0   
    else:
        RED = int(red.get())
        if RED > 255:
            RED = 255

    if green.get() == '':
        GREEN = 0
    else:
        GREEN = int(green.get())
        if GREEN > 255:
            GREEN = 255

    if blue.get() == '':
        BLUE = 0
    else:
        BLUE = int(blue.get())
        if BLUE > 255:
            BLUE = 255

    print('RED {} GREEN {} BLUE {}'.format(RED, GREEN, BLUE))
    print(type(RED))

    SA.colorPicture(RED, GREEN, BLUE)
    label_colorir.config(text= "Concluído", fg = "green")

def salvar():
    global salvar_pasta
    salvar_pasta = filedialog.askdirectory(title="Selecione uma pasta")
    SA.set_folder_save(salvar_pasta)
    SA.savePicture()
    label_salvar.config(text= "Concluído", fg = "green")
    print('salvo em {}'.format(salvar_pasta))

def botaoteste():
    print('botao')

def executar_video():
    SA.video()

color1 = "#FFFFFF"

window  = tk.Tk()
window.title("Speclke Analiser")
window.config(bg=color1)
window.geometry("390x515")
window.resizable(width=False, height=False)

label1 = tk.Label(window, text="Speclke Analiser - Analisador de Atividade de Speclke")
label1.place(x=7, y=15)

label2 = tk.Label(window, text="Análise de Fotos:")
label2.place(x=20, y=50)

botao1 = tk.Button(window, text="Selecionar Pasta de Arquivos", command=selecionar_pasta)
botao1.place(x=25, y=80)

botao2 = tk.Button(window, text="Executar", command=executar)
botao2.place(x=255, y=80)

label3 = tk.Label(window, text="Progresso: ")
label3.place(x=40, y=120)

label_prog = tk.Label(window, text = "Selecione uma pasta e Execute.", fg = "red")
label_prog.place(x=120, y=120)

label4 = tk.Label(window, text="Nível de Cores (1 a 255): ")
label4.place(x=40, y=150)

#
# 
# 

valor1 = tk.StringVar()
valor2 = tk.StringVar()
valor3 = tk.StringVar()
valor1.set("255")
valor2.set("127")
valor3.set("63")

vcmd = (window.register(apenas_numeros), "%P")

#entrada vermelho
label_r = tk.Label(window, text="Vermelho:")
label_r.place(x=50 , y= 180)

red = tk.Entry(window, validate="key", validatecommand=vcmd, textvariable=valor1)
red.place(x=130 , y= 180)

#entrada verde
label_g = tk.Label(window, text="Verde:")
label_g.place(x=50 , y= 210)

green = tk.Entry(window, validate="key", validatecommand=vcmd, textvariable=valor2)
green.place(x=130 , y= 210)

#entrada azul
label_b = tk.Label(window, text="Azul:")
label_b.place(x=50 , y= 240)

blue = tk.Entry(window, validate="key", validatecommand=vcmd, textvariable=valor3)
blue.place(x=130 , y= 240)

botao3 = tk.Button(window, text="Colorir", command=colorir)
botao3.place(x=25 , y= 280)

label_colorir = tk.Label(window, text = "", bg = color1)
label_colorir.place(x=100, y=285)

botao4 = tk.Button(window, text="Salvar", command=salvar)
botao4.place(x=25 , y= 320)

label_salvar = tk.Label(window, text = "", bg = color1)
label_salvar.place(x=100, y=325)

# video

label5 = tk.Label(window, text="Análise em Vídeo")
label5.place(x=20, y=370)

botao5 = tk.Button(window, text="Selecionar Pasta de Arquivos", command=selecionar_pasta)
botao5.place(x=25, y=400)

botao6 = tk.Button(window, text="Executar e Salvar", command=executar_video)
botao6.place(x=25, y=440)

label7 = tk.Label(window, text="Progresso: ")
label7.place(x=40, y=480)

label_salvar2 = tk.Label(window, text = "", bg = color1)
label_salvar2.place(x=120, y=480)

# video

window.mainloop()

