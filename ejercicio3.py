import math
import tkinter as tk
from tkinter import scrolledtext


class CalculosNumericos:
    @staticmethod
    def calcular_logaritmo_neperiano(valor: float) -> str:
        try:
            if valor <= 0:
                raise ArithmeticError("El valor debe ser un número positivo")
            resultado = math.log(valor)
            return f"Logaritmo neperiano = {resultado:.6f}"
        except ArithmeticError:
            return "El valor debe ser un número positivo para calcular el logaritmo"
        except TypeError:
            return "El valor debe ser numérico para calcular el logaritmo"

    @staticmethod
    def calcular_raiz_cuadrada(valor: float) -> str:
        try:
            if valor < 0:
                raise ArithmeticError("El valor debe ser un número positivo")
            resultado = math.sqrt(valor)
            return f"Raíz cuadrada = {resultado:.6f}"
        except ArithmeticError:
            return "El valor debe ser un número positivo para calcular la raíz cuadrada"
        except TypeError:
            return "El valor debe ser numérico para calcular la raíz cuadrada"


class InterfazCalculosNumericos:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Ejercicio 6.6 - Cálculos Numéricos (Catchs Múltiples)")
        self.root.geometry("500x360")
        self.root.resizable(False, False)
        self._construir_ui()

    def _construir_ui(self):
        tk.Label(
            self.root,
            text="Ejercicio 6.6: Cálculos Numéricos y Excepciones Múltiples",
            font=("Arial", 12, "bold"),
        ).pack(pady=(12, 8))

        frame_entrada = tk.LabelFrame(self.root, text="Entrada de Datos", padx=15, pady=12)
        frame_entrada.pack(fill="x", padx=20, pady=5)

        tk.Label(frame_entrada, text="Valor numérico:").grid(row=0, column=0, sticky="w", pady=4)
        self.entry_valor = tk.Entry(frame_entrada, width=25)
        self.entry_valor.grid(row=0, column=1, padx=10, pady=4)
        self.entry_valor.insert(0, "-200")

        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        tk.Button(
            frame_botones,
            text="Calcular",
            command=self.ejecutar_calculos,
            bg="#1565c0",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=14,
            pady=4,
        ).pack(side="left", padx=5)

        tk.Button(
            frame_botones,
            text="Limpiar",
            command=self.limpiar,
            padx=14,
            pady=4,
        ).pack(side="left", padx=5)

        frame_salida = tk.LabelFrame(self.root, text="Resultados / Excepciones Capturadas", padx=10, pady=10)
        frame_salida.pack(fill="both", expand=True, padx=20, pady=(0, 15))

        self.txt_salida = scrolledtext.ScrolledText(
            frame_salida, height=6, font=("Consolas", 10), state="disabled", bg="#f8f9fa"
        )
        self.txt_salida.pack(fill="both", expand=True)

    def _mostrar_salida(self, texto: str) -> None:
        self.txt_salida.config(state="normal")
        self.txt_salida.delete("1.0", tk.END)
        self.txt_salida.insert(tk.END, texto)
        self.txt_salida.config(state="disabled")

    def ejecutar_calculos(self) -> None:
        entrada = self.entry_valor.get().strip()
        try:
            valor = float(entrada)
            res_log = CalculosNumericos.calcular_logaritmo_neperiano(valor)
            res_raiz = CalculosNumericos.calcular_raiz_cuadrada(valor)
            self._mostrar_salida(f"Valor numérico = {valor}\n{res_log}\n{res_raiz}")
        except ValueError:
            self._mostrar_salida(
                "Excepción de entrada (ValueError):\n"
                "El valor debe ser numérico para calcular el logaritmo\n"
                "El valor debe ser numérico para calcular la raíz cuadrada"
            )

    def limpiar(self) -> None:
        self.entry_valor.delete(0, tk.END)
        self._mostrar_salida("")


if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazCalculosNumericos(ventana)
    ventana.mainloop()
