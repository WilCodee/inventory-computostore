import tkinter as tk
from tkinter import messagebox

from app.controllers.user_controller import UserController


class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Logo
        self.logo = tk.PhotoImage(file="app/assets/logo.png")
        self.logo_label = tk.Label(self.root, image=self.logo)
        self.logo_label.pack(pady=10)

        # Username
        self.username_label = tk.Label(self.root, text="Usuario:")
        self.username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        # Password
        self.password_label = tk.Label(self.root, text="Contraseña:")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        # Login Button
        self.login_button = tk.Button(self.root, text="Iniciar Sesión", command=self.login)
        self.login_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            # Verificar usuario usando el controlador
            user = UserController.verification_user(username, password)
            if user:
                messagebox.showinfo("Éxito", f"Inicio de sesión exitoso.\n!Bienvenido, {user.name}!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
