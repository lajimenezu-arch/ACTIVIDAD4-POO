import tkinter as tk
from tkinter import messagebox, scrolledtext


class Vendedor:
    def __init__(self, nombre: str, apellidos: str):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad: int | None = None

    def imprimir(self) -> str:
        return (
            f"Nombre del vendedor = {self.nombre}\n"
            f"Apellidos del vendedor = {self.apellidos}\n"
            f"Edad del vendedor = {self.edad}"
        )

    def verificar_edad(self, edad: int) -> None:
        if edad < 0 or edad > 120:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        self.edad = edad


class InterfazVendedor:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Ejercicio 6.5 - Clase Vendedor (Lanzamiento de Excepciones)")
        self.root.geometry("470x390")
        self.root.resizable(False, False)
        self._construir_ui()

    def _construir_ui(self):
        tk.Label(
            self.root,
            text="Ejercicio 6.5: Registro y Validación de Vendedor",
            font=("Arial", 12, "bold"),
        ).pack(pady=(12, 8))

        frame_form = tk.LabelFrame(self.root, text="Datos del Vendedor", padx=15, pady=12)
        frame_form.pack(fill="x", padx=20, pady=5)

        tk.Label(frame_form, text="Nombre del vendedor:").grid(row=0, column=0, sticky="w", pady=4)
        self.entry_nombre = tk.Entry(frame_form, width=28)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=4)

        tk.Label(frame_form, text="Apellidos del vendedor:").grid(row=1, column=0, sticky="w", pady=4)
        self.entry_apellidos = tk.Entry(frame_form, width=28)
        self.entry_apellidos.grid(row=1, column=1, padx=10, pady=4)

        tk.Label(frame_form, text="Edad del vendedor:").grid(row=2, column=0, sticky="w", pady=4)
        self.entry_edad = tk.Entry(frame_form, width=28)
        self.entry_edad.grid(row=2, column=1, padx=10, pady=4)

        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        tk.Button(
            frame_botones,
            text="Registrar y Verificar Vendedor",
            command=self.registrar_vendedor,
            bg="#1565c0",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=4,
        ).pack(side="left", padx=5)

        tk.Button(
            frame_botones,
            text="Limpiar",
            command=self.limpiar,
            padx=10,
            pady=4,
        ).pack(side="left", padx=5)

        frame_salida = tk.LabelFrame(self.root, text="Salida / Excepciones Capturadas", padx=10, pady=10)
        frame_salida.pack(fill="both", expand=True, padx=20, pady=(0, 15))

        self.txt_salida = scrolledtext.ScrolledText(
            frame_salida, height=6, font=("Consolas", 10), state="disabled", bg="#f8f9fa"
        )
        self.txt_salida.pack(fill="both", expand=True)

    def _mostrar_texto(self, mensaje: str) -> None:
        self.txt_salida.config(state="normal")
        self.txt_salida.delete("1.0", tk.END)
        self.txt_salida.insert(tk.END, mensaje)
        self.txt_salida.config(state="disabled")

    def registrar_vendedor(self) -> None:
        nombre = self.entry_nombre.get().strip()
        apellidos = self.entry_apellidos.get().strip()
        edad_texto = self.entry_edad.get().strip()

        if not nombre or not apellidos:
            messagebox.showwarning("Campos incompletos", "Por favor ingresa el nombre y los apellidos del vendedor.")
            return

        try:
            edad = int(edad_texto)
            vendedor = Vendedor(nombre, apellidos)
            vendedor.verificar_edad(edad)
            self._mostrar_texto(vendedor.imprimir())
        except ValueError as e:
            if "invalid literal for int()" in str(e):
                self._mostrar_texto("Error: La edad debe ser un número entero válido.")
            else:
                self._mostrar_texto(f"Excepción lanzada (ValueError):\n{e}")

    def limpiar(self) -> None:
        self.entry_nombre.delete(0, tk.END)
        self.entry_apellidos.delete(0, tk.END)
        self.entry_edad.delete(0, tk.END)
        self._mostrar_texto("")


if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazVendedor(ventana)
    ventana.mainloop()
