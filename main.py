import os
import sys
import tkinter as tk

from dotenv import load_dotenv


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


load_dotenv(resource_path(".env"))  # Esto carga las variables desde .env

"""
Archivo principal para iniciar la aplicación Inventory ComputoStore.
"""

if not os.getenv("MONGO_URI") or not os.getenv("MONGO_DB_NAME"):
    raise EnvironmentError("Falta la variable de entorno MONGO_URI o MONGO_DB_NAME en el archivo .env")

if __name__ == "__main__":
    from app.views.login_view import LoginView

    root = tk.Tk()
    app = LoginView(root)
    root.mainloop()
