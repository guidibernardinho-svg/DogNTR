import tkinter as tk
import threading
import socket

# =========================
# BACKEND (simulado)
# =========================
def start_server():
    print("🚀 DogNTR server iniciado")

    # aqui depois entra stream do 3DS
    # socket real fica aqui

# =========================
# UI
# =========================
root = tk.Tk()
root.title("🎮 DogNTR")
root.geometry("600x400")

# =========================
# TELA DO 3DS (placeholder)
# =========================
screen = tk.Label(root, text="📺 Tela do 3DS aqui", bg="black", fg="white", width=50, height=10)
screen.pack(pady=10)

# =========================
# CONTROLES
# =========================
frame = tk.Frame(root)
frame.pack()

def press(btn):
    print(f"🎮 {btn} pressionado")

tk.Button(frame, text="A", width=5, command=lambda: press("A")).grid(row=0, column=0)
tk.Button(frame, text="B", width=5, command=lambda: press("B")).grid(row=0, column=1)
tk.Button(frame, text="X", width=5, command=lambda: press("X")).grid(row=0, column=2)
tk.Button(frame, text="Y", width=5, command=lambda: press("Y")).grid(row=0, column=3)

# =========================
# THREAD DO SERVER
# =========================
threading.Thread(target=start_server, daemon=True).start()

# =========================
# LOOP UI
# =========================
root.mainloop()
