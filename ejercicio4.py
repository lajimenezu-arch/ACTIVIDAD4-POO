import tkinter as tk
from tkinter import messagebox, scrolledtext


class Programador:
    def __init__(self, nombre: str, apellidos: str):
        self.nombre = nombre
        self.apellidos = apellidos


class EquipoMaratonProgramacion:
    def __init__(self, nombre_equipo: str, universidad: str, lenguaje_programacion: str):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.programadores: list[Programador] = []
        self.tamano_equipo: int = 0

    def esta_lleno(self) -> bool:
        return self.tamano_equipo == 3

    def anadir(self, programador: Programador) -> None:
        if self.esta_lleno():
            raise Exception("El equipo está completo. No se pudo agregar programador.")
        self.programadores.append(programador)
        self.tamano_equipo += 1

    @staticmethod
    def validar_campo(campo: str) -> None:
        if not campo:
            raise Exception("El campo no puede estar vacío.")
        for caracter in campo:
            if caracter.isdigit():
                raise Exception("El nombre no puede tener dígitos.")
        if len(campo) > 20:
            raise Exception("La longitud no debe ser superior a 20 caracteres.")


class InterfazMaraton:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Ejercicio 6.7 - Validación de Campos (Maratón de Programación)")
        self.root.geometry("520x520")
        self.root.resizable(False, False)
        self.equipo: EquipoMaratonProgramacion | None = None
        self._construir_ui()

    def _construir_ui(self):
        tk.Label(
            self.root,
            text="Ejercicio 6.7: Equipo de Maratón de Programación",
            font=("Arial", 12, "bold"),
        ).pack(pady=(10, 6))

        # Sección 1: Datos del equipo
        frame_eq = tk.LabelFrame(self.root, text="1. Datos del Equipo", padx=12, pady=8)
        frame_eq.pack(fill="x", padx=20, pady=4)

        tk.Label(frame_eq, text="Nombre del equipo:").grid(row=0, column=0, sticky="w", pady=3)
        self.entry_equipo = tk.Entry(frame_eq, width=28)
        self.entry_equipo.grid(row=0, column=1, padx=8, pady=3)

        tk.Label(frame_eq, text="Universidad:").grid(row=1, column=0, sticky="w", pady=3)
        self.entry_universidad = tk.Entry(frame_eq, width=28)
        self.entry_universidad.grid(row=1, column=1, padx=8, pady=3)

        tk.Label(frame_eq, text="Lenguaje de programación:").grid(row=2, column=0, sticky="w", pady=3)
        self.entry_lenguaje = tk.Entry(frame_eq, width=28)
        self.entry_lenguaje.grid(row=2, column=1, padx=8, pady=3)

        tk.Button(
            frame_eq,
            text="Crear Equipo",
            command=self.crear_equipo,
            bg="#1565c0",
            fg="white",
            font=("Arial", 9, "bold"),
            padx=10,
        ).grid(row=3, column=0, columnspan=2, pady=(6, 2))

        # Sección 2: Datos del programador
        frame_prog = tk.LabelFrame(self.root, text="2. Añadir Integrante (Máximo 3)", padx=12, pady=8)
        frame_prog.pack(fill="x", padx=20, pady=4)

        tk.Label(frame_prog, text="Nombre del integrante:").grid(row=0, column=0, sticky="w", pady=3)
        self.entry_nom_prog = tk.Entry(frame_prog, width=28)
        self.entry_nom_prog.grid(row=0, column=1, padx=8, pady=3)

        tk.Label(frame_prog, text="Apellidos del integrante:").grid(row=1, column=0, sticky="w", pady=3)
        self.entry_ape_prog = tk.Entry(frame_prog, width=28)
        self.entry_ape_prog.grid(row=1, column=1, padx=8, pady=3)

        frame_btns = tk.Frame(frame_prog)
        frame_btns.grid(row=2, column=0, columnspan=2, pady=(6, 2))

        tk.Button(
            frame_btns,
            text="Añadir Programador",
            command=self.agregar_programador,
            bg="#2e7d32",
            fg="white",
            font=("Arial", 9, "bold"),
            padx=10,
        ).pack(side="left", padx=5)

        tk.Button(
            frame_btns,
            text="Reiniciar Todo",
            command=self.reiniciar,
            padx=10,
        ).pack(side="left", padx=5)

        # Sección 3: Consola de salida
        frame_salida = tk.LabelFrame(self.root, text="Estado del Equipo / Excepciones", padx=10, pady=8)
        frame_salida.pack(fill="both", expand=True, padx=20, pady=(4, 12))

        self.txt_salida = scrolledtext.ScrolledText(
            frame_salida, height=8, font=("Consolas", 9), state="disabled", bg="#f8f9fa"
        )
        self.txt_salida.pack(fill="both", expand=True)

    def _actualizar_consola(self, mensaje_extra: str = "") -> None:
        self.txt_salida.config(state="normal")
        self.txt_salida.delete("1.0", tk.END)
        if self.equipo:
            self.txt_salida.insert(
                tk.END,
                f"Equipo: {self.equipo.nombre_equipo} | Univ: {self.equipo.universidad} | Lenguaje: {self.equipo.lenguaje_programacion}\n",
            )
            self.txt_salida.insert(tk.END, f"Integrantes ({self.equipo.tamano_equipo}/3):\n")
            for idx, p in enumerate(self.equipo.programadores, start=1):
                self.txt_salida.insert(tk.END, f"  {idx}. {p.nombre} {p.apellidos}\n")
        if mensaje_extra:
            self.txt_salida.insert(tk.END, f"\n{mensaje_extra}")
        self.txt_salida.config(state="disabled")

    def crear_equipo(self) -> None:
        nombre = self.entry_equipo.get().strip()
        univ = self.entry_universidad.get().strip()
        leng = self.entry_lenguaje.get().strip()

        if not nombre or not univ or not leng:
            messagebox.showwarning("Campos incompletos", "Por favor completa todos los datos del equipo.")
            return

        self.equipo = EquipoMaratonProgramacion(nombre, univ, leng)
        self._actualizar_consola("Equipo creado correctamente. Ahora puedes añadir entre 2 y 3 programadores.")

    def agregar_programador(self) -> None:
        if self.equipo is None:
            messagebox.showwarning("Sin equipo", "Primero debes crear un equipo de maratón.")
            return

        nombre = self.entry_nom_prog.get().strip()
        apellidos = self.entry_ape_prog.get().strip()

        try:
            EquipoMaratonProgramacion.validar_campo(nombre)
            EquipoMaratonProgramacion.validar_campo(apellidos)
            programador = Programador(nombre, apellidos)
            self.equipo.anadir(programador)

            self.entry_nom_prog.delete(0, tk.END)
            self.entry_ape_prog.delete(0, tk.END)
            estado = (
                "Equipo completo (3/3 integrantes)."
                if self.equipo.esta_lleno()
                else "Programador añadido exitosamente."
            )
            self._actualizar_consola(estado)
        except Exception as e:
            self._actualizar_consola(f"Excepción capturada:\n{e}")

    def reiniciar(self) -> None:
        self.equipo = None
        self.entry_equipo.delete(0, tk.END)
        self.entry_universidad.delete(0, tk.END)
        self.entry_lenguaje.delete(0, tk.END)
        self.entry_nom_prog.delete(0, tk.END)
        self.entry_ape_prog.delete(0, tk.END)
        self._actualizar_consola("")


if __name__ == "__main__":
    ventana = tk.Tk()
    app = InterfazMaraton(ventana)
    ventana.mainloop()
