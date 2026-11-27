import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext


class LeerArchivo:
    def leer_contenido(self, ruta_archivo: str) -> str:
        lineas_leidas = []
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                linea = archivo.readline()
                while linea != "":
                    lineas_leidas.append(linea.rstrip("\n"))
                    linea = archivo.readline()
            return "\n".join(lineas_leidas)
        except OSError as e:
            raise IOError("No se pudo leer el archivo.") from e

    def crear_archivo_prueba(self, ruta_archivo: str = "prueba.txt") -> str:
        try:
            with open(ruta_archivo, "w", encoding="utf-8") as archivo:
                for i in range(1, 11):
                    archivo.write(f"Linea {i}\n")
            return os.path.abspath(ruta_archivo)
        except OSError as e:
            raise IOError("No se pudo crear el archivo de prueba.") from e


class InterfazLeerArchivo:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Ejercicio 6.8 - Lectura de Archivos (LeerArchivo)")
        self.root.geometry("520x420")
        self.root.resizable(False, False)
        self.lector = LeerArchivo()
        self._construir_ui()

    def _construir_ui(self):
        tk.Label(
            self.root,
            text="Ejercicio 6.8: Lectura de Archivos de Texto",
            font=("Arial", 12, "bold"),
        ).pack(pady=(12, 8))

        frame_ruta = tk.LabelFrame(self.root, text="Ubicación del Archivo (.txt)", padx=12, pady=10)
        frame_ruta.pack(fill="x", padx=20, pady=5)

        tk.Label(frame_ruta, text="Ruta:").grid(row=0, column=0, sticky="w")
        self.entry_ruta = tk.Entry(frame_ruta, width=42)
        self.entry_ruta.grid(row=0, column=1, padx=6)
        self.entry_ruta.insert(0, "C:/prueba.txt")

        tk.Button(
            frame_ruta,
            text="Examinar...",
            command=self.examinar_archivo,
            padx=8,
        ).grid(row=0, column=2)

        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)

        tk.Button(
            frame_botones,
            text="Leer Archivo",
            command=self.ejecutar_lectura,
            bg="#1565c0",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=12,
            pady=4,
        ).pack(side="left", padx=5)

        tk.Button(
            frame_botones,
            text="Generar prueba.txt",
            command=self.generar_prueba,
            bg="#2e7d32",
            fg="white",
            font=("Arial", 9, "bold"),
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

        frame_salida = tk.LabelFrame(self.root, text="Contenido del Archivo / Excepciones", padx=10, pady=10)
        frame_salida.pack(fill="both", expand=True, padx=20, pady=(0, 15))

        self.txt_contenido = scrolledtext.ScrolledText(
            frame_salida, height=10, font=("Consolas", 10), state="disabled", bg="#f8f9fa"
        )
        self.txt_contenido.pack(fill="both", expand=True)

    def _mostrar_texto(self, texto: str) -> None:
        self.txt_contenido.config(state="normal")
        self.txt_contenido.delete("1.0", tk.END)
        self.txt_contenido.insert(tk.END, texto)
        self.txt_contenido.config(state="disabled")

    def examinar_archivo(self) -> None:
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo de texto",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")],
        )
        if ruta:
            self.entry_ruta.delete(0, tk.END)
            self.entry_ruta.insert(0, ruta)

    def generar_prueba(self) -> None:
        try:
            ruta_creada = self.lector.crear_archivo_prueba("prueba.txt")
            self.entry_ruta.delete(0, tk.END)
            self.entry_ruta.insert(0, ruta_creada)
            self._mostrar_texto(f"Archivo de prueba generado en:\n{ruta_creada}\n\nPresiona 'Leer Archivo' para visualizar su contenido.")
        except IOError as e:
            self._mostrar_texto(str(e))

    def ejecutar_lectura(self) -> None:
        ruta = self.entry_ruta.get().strip()
        if not ruta:
            messagebox.showwarning("Ruta vacía", "Por favor ingresa o selecciona la ruta de un archivo.")
            return

        try:
            contenido = self.lector.leer_contenido(ruta)
            self._mostrar_texto(contenido)
        except IOError as e:
            self._mostrar_texto(str(e))

    def limpiar(self) -> None:
        self._mostrar_texto("")


if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazLeerArchivo(ventana)
    ventana.mainloop()
