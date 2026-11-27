import tkinter as tk
from tkinter import scrolledtext


class PruebaExcepciones:
    def ejecutar_pruebas(self, divisor: float = 0, usar_objeto_nulo: bool = True) -> list[str]:
        salida = []

        # Primer bloque try
        try:
            salida.append("Ingresando al primer try")
            cociente = 10000 / divisor
            salida.append(f"Después de la división (Cociente = {cociente})")
        except ZeroDivisionError:
            salida.append("División por cero")
        finally:
            salida.append("Ingresando al primer finally")

        # Segundo bloque try
        try:
            salida.append("Ingresando al segundo try")
            objeto = None if usar_objeto_nulo else "Objeto válido"
            _ = objeto.upper()  # type: ignore
            salida.append("Imprimiendo objeto")
        except ZeroDivisionError:
            salida.append("División por cero")
        except Exception:
            salida.append("Ocurrió una excepción")
        finally:
            salida.append("Ingresando al segundo finally")

        return salida


class InterfazPruebaExcepciones:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Ejercicio 6.4 - PruebaExcepciones")
        self.root.geometry("480x400")
        self.root.resizable(False, False)
        self.prueba = PruebaExcepciones()
        self._construir_ui()

    def _construir_ui(self):
        tk.Label(
            self.root,
            text="Ejercicio 6.4: Clase PruebaExcepciones",
            font=("Arial", 13, "bold"),
        ).pack(pady=(12, 5))

        frame_config = tk.LabelFrame(self.root, text="Parámetros de Ejecución", padx=12, pady=10)
        frame_config.pack(fill="x", padx=20, pady=5)

        tk.Label(frame_config, text="Divisor para 10000 / divisor:").grid(row=0, column=0, sticky="w")
        self.entry_divisor = tk.Entry(frame_config, width=10)
        self.entry_divisor.grid(row=0, column=1, padx=8)
        self.entry_divisor.insert(0, "0")

        self.var_nulo = tk.BooleanVar(value=True)
        tk.Checkbutton(
            frame_config,
            text="Asignar objeto = None (null) en el segundo try",
            variable=self.var_nulo,
        ).grid(row=1, column=0, columnspan=2, sticky="w", pady=(6, 0))

        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        tk.Button(
            frame_botones,
            text="Ejecutar PruebaExcepciones",
            command=self.ejecutar,
            bg="#1565c0",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=4,
        ).pack(side="left", padx=5)

        tk.Button(
            frame_botones,
            text="Limpiar Consola",
            command=self.limpiar,
            padx=10,
            pady=4,
        ).pack(side="left", padx=5)

        frame_salida = tk.LabelFrame(self.root, text="Resultado en Pantalla", padx=10, pady=10)
        frame_salida.pack(fill="both", expand=True, padx=20, pady=(0, 15))

        self.txt_consola = scrolledtext.ScrolledText(
            frame_salida, height=8, font=("Consolas", 10), state="disabled", bg="#f8f9fa"
        )
        self.txt_consola.pack(fill="both", expand=True)

    def ejecutar(self):
        try:
            divisor = float(self.entry_divisor.get())
        except ValueError:
            divisor = 0.0
            self.entry_divisor.delete(0, tk.END)
            self.entry_divisor.insert(0, "0")

        mensajes = self.prueba.ejecutar_pruebas(divisor=divisor, usar_objeto_nulo=self.var_nulo.get())

        self.txt_consola.config(state="normal")
        self.txt_consola.delete("1.0", tk.END)
        for linea in mensajes:
            self.txt_consola.insert(tk.END, linea + "\n")
        self.txt_consola.config(state="disabled")

    def limpiar(self):
        self.txt_consola.config(state="normal")
        self.txt_consola.delete("1.0", tk.END)
        self.txt_consola.config(state="disabled")


if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazPruebaExcepciones(ventana)
    ventana.mainloop()
