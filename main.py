import customtkinter as tk
import pyperclip

janela = tk.CTk()
janela.geometry("605x583+367+19")

n_pedidos = 0

frame = tk.CTkFrame(janela)
frame.pack(padx=10,pady=10)

tabview_criar_pedido = tk.CTkTabview(frame)
tabview_criar_pedido.pack(padx=10,pady=10)

#ciar pedido
tab_criar_pedido = tabview_criar_pedido.add('Criar pedido')
tabview_criar_pedido.set('Criar pedido')

tab_criar_pedido.grid_rowconfigure(0, weight=0)
tab_criar_pedido.grid_columnconfigure(2, weight=1)
tab_criar_pedido.grid_columnconfigure(1, weight=1)
tab_criar_pedido.grid_columnconfigure(0, weight=1)

label_tab1_criar_pedido = tk.CTkLabel(tab_criar_pedido, text='Criar pedido', font=("",16))
label_tab1_criar_pedido.grid(column=1,row=0)


tabview_montar = tk.CTkTabview(tab_criar_pedido)
tabview_montar.grid(row=0, column=1, padx=10,pady=10)
tab_montar_pedido = tabview_montar.add('Montar do zero')
tabview_montar.set('Montar do zero')

tab_sabores_prontos = tabview_montar.add('Sabores prontos')

sabores_prontos_value = tk.IntVar()

sabor_4queijos = tk.CTkRadioButton(tab_sabores_prontos, text='4 Queijos', variable=sabores_prontos_value, value=0)
sabor_4queijos.pack(padx=10, pady=10)

sabor_calabresa = tk.CTkRadioButton(tab_sabores_prontos, text='Calabresa', variable=sabores_prontos_value, value=1)
sabor_calabresa.pack(padx=10, pady=10)

sabor_frango_catupery = tk.CTkRadioButton(tab_sabores_prontos, text='Frango catupery', variable=sabores_prontos_value, value=2)
sabor_frango_catupery.pack(padx=10, pady=10)

def gerar_pe_pronto():
    global n_pedidos
    n_pedidos += 1
    sabores_value = int(sabores_prontos_value.get())
    output_script_pedido.configure(state='normal')
    pedidos = (f'Pedido: {n_pedidos} ')
    output_script_pedido.insert('0.0', '###########################\n')
    if sabores_value == 0:
        output_script_pedido.insert('0.0', 'Queijo\nMolho de tomate simples\nÓregano\n')
        output_script_pedido.insert('0.0', 'Pizza de 4 queijos\n')
    elif sabores_value == 1:
        output_script_pedido.insert('0.0', 'Queijo\nCalabresa\nMolho de tomate simples\nCebola\n')
        output_script_pedido.insert('0.0', 'Pizza de calabresa\n')
    elif sabores_value == 2:
        output_script_pedido.insert('0.0', 'Queijo\nMolho branco\nFrango\nCatupery\n')
        output_script_pedido.insert('0.0', 'Pizza com frango catupery\n')
    output_script_pedido.insert('0.0', pedidos)
    output_script_pedido.insert('0.0', '###########################\n')
    output_script_pedido.configure(state='disabled')

    

gerar_pedido_pronto = tk.CTkButton(tab_sabores_prontos, text='Gerar pedido', command=gerar_pe_pronto)
gerar_pedido_pronto.pack(padx=10, pady=10, side='bottom')

# montar do zero
#frame das bordas ##################################
label_tab1_bordas = tk.CTkLabel(tab_montar_pedido, text='Bordas', font=('',20))
label_tab1_bordas.grid(column=0, row=1)

frame_bordas = tk.CTkFrame(tab_montar_pedido)
frame_bordas.grid(column=0, row=2, padx=10, pady=10)

radio_borda_var = tk.IntVar()

borda_sem_borda = tk.CTkRadioButton(frame_bordas, text='Borda simples', variable=radio_borda_var, value=0)
borda_sem_borda.pack(padx=10, pady=10)

borda_catupery = tk.CTkRadioButton(frame_bordas, text='Borda catupery', variable=radio_borda_var, value=1)
borda_catupery.pack(padx=10, pady=10)

borda_cheddar = tk.CTkRadioButton(frame_bordas, text='Borda cheddar', variable=radio_borda_var, value=2)
borda_cheddar.pack(padx=10, pady=10)

#frame dos molhos #################################
label_tab1_molhos = tk.CTkLabel(tab_montar_pedido, text="Molhos", font=('',20))
label_tab1_molhos.grid(column=1, row=1)

frame_molhos = tk.CTkFrame(tab_montar_pedido)
frame_molhos.grid(column=1, row=2, padx=10, pady=10)

radio_molho_var = tk.IntVar()

molho_simples = tk.CTkRadioButton(frame_molhos, text='Molho de tomate simples', variable=radio_molho_var, value=0)
molho_simples.pack(padx=10, pady=10)

molho_ervas = tk.CTkRadioButton(frame_molhos, text='Molho de tomate com ervas', variable=radio_molho_var, value=1)
molho_ervas.pack(padx=10, pady=10)

molho_branco = tk.CTkRadioButton(frame_molhos, text='Molho branco', variable=radio_molho_var, value=2)
molho_branco.pack(padx=10, pady=10)

#frame dos igredientes ################################
label_tab1_igredientes = tk.CTkLabel(tab_montar_pedido, text="Igredientes", font=('',20))
label_tab1_igredientes.grid(column=2, row=1, padx=10, pady=10)

frame_igredientes = tk.CTkFrame(tab_montar_pedido)
frame_igredientes.grid(column=2, row=2, padx=10, pady=10)

igrediente_queijo_var = tk.StringVar()
igrediente_presunto_var = tk.StringVar()
igrediente_cogumelos_var = tk.StringVar()
igrediente_tomate_var = tk.StringVar() 
igrediente_cebola_var = tk.StringVar()
igrediente_calabresa_var = tk.StringVar()
igrediente_azeitona_var = tk.StringVar()

igrediente_queijo = tk.CTkCheckBox(frame_igredientes, text='Queijo', variable=igrediente_queijo_var, onvalue='on', offvalue='off')
igrediente_queijo.pack(padx=10, pady=10)

igrediente_presunto = tk.CTkCheckBox(frame_igredientes, text='Presunto', variable=igrediente_presunto_var, onvalue='on', offvalue='off')
igrediente_presunto.pack(padx=10, pady=10)

igrediente_cogumelos = tk.CTkCheckBox(frame_igredientes, text='Cogumelos', variable=igrediente_cogumelos_var, onvalue='on', offvalue='off')
igrediente_cogumelos.pack(padx=10, pady=10)

igrediente_tomate = tk.CTkCheckBox(frame_igredientes, text='Tomate', variable=igrediente_tomate_var, onvalue='on', offvalue='off')
igrediente_tomate.pack(padx=10, pady=10)

igrediente_cebola = tk.CTkCheckBox(frame_igredientes, text='Cebola', variable=igrediente_cebola_var, onvalue='on', offvalue='off')
igrediente_cebola.pack(padx=10, pady=10)

igrediente_calabresa = tk.CTkCheckBox(frame_igredientes, text='Calabresa', variable=igrediente_calabresa_var, onvalue='on', offvalue='off')
igrediente_calabresa.pack(padx=10, pady=10)

igrediente_azeitona = tk.CTkCheckBox(frame_igredientes, text='Azeitona', variable=igrediente_azeitona_var, onvalue='on', offvalue='off')
igrediente_azeitona.pack(padx=10, pady=10)


def run_gerar_pedido_montado():
    global n_pedidos
    n_pedidos += 1
    output_script_pedido.configure(state='normal')
    borda_value = int(radio_borda_var.get())
    molho_value = int(radio_molho_var.get())
    azeitona_value = igrediente_azeitona_var.get()
    queijo_value = igrediente_queijo_var.get()
    presunto_value = igrediente_presunto_var.get()
    cebola_value = igrediente_cebola_var.get()
    tomate_value = igrediente_tomate_var.get()
    calabresa_value = igrediente_calabresa_var.get()
    cogumelos_value = igrediente_cogumelos_var.get()
    #cada print deve sair no output de script
    
    pedidos = (f'Pedido: {n_pedidos}\n')
    output_script_pedido.insert('0.0', '###########################\n')
    
    if borda_value == 0:
        output_script_pedido.insert('0.0', "Borda simples\n")
    elif borda_value == 1:
        output_script_pedido.insert('0.0', "Borda catupery\n")
    elif borda_value == 2:
        output_script_pedido.insert('0.0', "Borda cheddar\n")
    if molho_value == 0:
        output_script_pedido.insert('0.0', "Molho simples\n")
    elif molho_value == 1:
        output_script_pedido.insert('0.0', "Molho com ervas\n")
    elif molho_value == 2:
        output_script_pedido.insert('0.0', "Molho branco\n")
    if azeitona_value == 'on':
        output_script_pedido.insert('0.0', 'Azeitona\n')
    if queijo_value == 'on':
        output_script_pedido.insert('0.0', 'Queijo\n')
    if presunto_value == 'on':
        output_script_pedido.insert('0.0', 'Presunto\n')
    if cebola_value == 'on':
        output_script_pedido.insert('0.0', 'Cebola\n')
    if tomate_value == 'on':
        output_script_pedido.insert('0.0', 'Tomate\n')
    if calabresa_value == 'on':
        output_script_pedido.insert('0.0', 'Calabresa\n')
    if cogumelos_value == 'on':
        output_script_pedido.insert('0.0', 'Cogumelos\n')
    output_script_pedido.insert('0.0', pedidos)
    output_script_pedido.insert('0.0', '###########################\n')
    output_script_pedido.configure(state='disabled')
gerar_pedido = tk.CTkButton(tab_montar_pedido, text='Gerar pedido', command=run_gerar_pedido_montado)
gerar_pedido.grid(column=1, row=3, padx=10, pady=10)

#tab script do pedido
tab_script_pedido = tabview_montar.add('Script do pedido')
output_script_pedido = tk.CTkTextbox(tab_script_pedido, width=400, height=400)

output_script_pedido.pack()

def copiar_script():
    pyperclip.copy(output_script_pedido.get('0.0', 'end'))

btn_copiar_output = tk.CTkButton(tab_script_pedido, text='Copiar Script', command=copiar_script)
btn_copiar_output.pack(padx=10, pady=10, side='left')

def limpar_prompt():
    output_script_pedido.configure(state='normal')
    output_script_pedido.delete('0.0', 'end')
    output_script_pedido.configure(state='disabled')


btn_limpar_output = tk.CTkButton(tab_script_pedido, text='Limpar', command=limpar_prompt)
btn_limpar_output.pack(padx=10, pady=10, side='right')


janela.mainloop()
