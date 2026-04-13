import traceback
import sys

try:
    from tkinter import Tk, Label
    root = Tk()
    root.title("Teste")
    label = Label(root, text="Janela abriu!")
    label.pack()
    root.update()
    print("Janela criada com sucesso!")
    root.after(3000, root.destroy)  # Fecha após 3 segundos
    root.mainloop()
    print("Fechou normalmente")
except Exception as e:
    print(f"ERRO: {e}")
    traceback.print_exc()
    input("Pressione Enter para sair...")
