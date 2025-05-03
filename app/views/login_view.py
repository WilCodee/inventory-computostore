import tkinter as tk
from tkinter import messagebox

from app.controllers.user_controller import UserController
from app.views.home_view import HomeView
from main import resource_path


class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión")
        self.root.geometry("350x200")
        self.root.resizable(False, False)

        # Contenedor principal (centrado)
        main_frame = tk.Frame(self.root)
        main_frame.pack(pady=10, padx=10, fill="both", expand=True)

        # Contenedor para el logo
        logo_frame = tk.Frame(main_frame)
        logo_frame.pack(side="left", padx=10, pady=10)

        # Logo
        self.logo = tk.PhotoImage(file=resource_path("app/assets/logo.png"))
        self.logo_label = tk.Label(logo_frame, image=self.logo)
        self.logo_label.pack()

        # Contenedor para los campos de texto y botones
        form_frame = tk.Frame(main_frame)
        form_frame.pack(side="left", padx=10, pady=10)

        # Username
        self.username_label = tk.Label(form_frame, text="Usuario:")
        self.username_label.pack(pady=5, anchor="w")
        self.username_entry = tk.Entry(form_frame)
        self.username_entry.pack(pady=5, fill="x")

        # Password
        self.password_label = tk.Label(form_frame, text="Contraseña:")
        self.password_label.pack(pady=5, anchor="w")
        self.password_entry = tk.Entry(form_frame, show="*")
        self.password_entry.pack(pady=5, fill="x")

        # Login Button
        self.login_button = tk.Button(form_frame, text="Iniciar Sesión", command=self.login)
        self.login_button.pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return

        try:
            # Verificar usuario usando el controlador
            user = UserController.verification_user(username, password)
            if user:
                self.root.destroy()
                root = tk.Tk()
                HomeView(root, user.name)
                root.mainloop()
        except Exception as e:
            messagebox.showerror("Error", str(e))
