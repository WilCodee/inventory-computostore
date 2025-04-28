import os
import tkinter as tk

from dotenv import load_dotenv

from app.views.login_view import LoginView

load_dotenv()  # Esto carga las variables desde .env

"""
Archivo principal para iniciar la aplicación Inventory ComputoStore.
"""

if not os.getenv("MONGO_URI") or not os.getenv("MONGO_DB_NAME"):
    raise EnvironmentError("Falta la variable de entorno MONGO_URI o MONGO_DB_NAME en el archivo .env")

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginView(root)
    root.mainloop()
