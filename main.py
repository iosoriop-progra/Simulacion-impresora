import tkinter as tk
from tkinter import messagebox
from cola import PrintTask
from impresora import Simulation

class ImpresoraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de una cola de una Impresión")
        self.root.geometry("600x650")
        self.root.configure(bg="#63CAE4") 

        # Lista temporal para guardar los trabajos que el usuario va creando
        self.lista_tareas_creadas = []
        
        
        self.fuente_texto = ("Century Gothic", 11)
        self.fuente_titulo = ("Century Gothic", 14, "bold")
        
        # Colores pastel del diseño, mis favoritos 
        self.AZUL_PASTEL = "#61B7F0"
        self.VERDE_PASTEL = "#80F863"
        self.AMARILLO_PASTEL = "#E3FF41"
        
        self.crear_componentes()

    def crear_componentes(self):
        # #titulo_aquí
        titulo = tk.Label(self.root, text="Simulación de Impresora", 
                          font=self.fuente_titulo, bg="#F2F4F4", fg="#153D64")
        titulo.pack(pady=15)

        
        frame_ingreso = tk.LabelFrame(self.root, text=" Registrar Trabajos de Impresión ", 
                                      font=self.fuente_texto, bg="#F2F4F4", fg="#2C3E50", padx=10, pady=10)
        frame_ingreso.pack(fill="x", padx=15, pady=5)

        # Entrada para ID 
        tk.Label(frame_ingreso, text="ID Documento:", font=self.fuente_texto, bg="#F2F4F4").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_id = tk.Entry(frame_ingreso, font=self.fuente_texto, width=15)
        self.entry_id.grid(row=0, column=1, padx=5, pady=5)

        # Esto me va a servir para las entrada para Páginas
        tk.Label(frame_ingreso, text="No. Páginas:", font=self.fuente_texto, bg="#F2F4F4").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_paginas = tk.Entry(frame_ingreso, font=self.fuente_texto, width=15)
        self.entry_paginas.grid(row=1, column=1, padx=5, pady=5)

        # Entrada para el señor Tiempo de llegada
        tk.Label(frame_ingreso, text="Segundo Llegada:", font=self.fuente_texto, bg="#F2F4F4").grid(row=2, column=0, sticky="w", pady=5)
        self.entry_llegada = tk.Entry(frame_ingreso, font=self.fuente_texto, width=15)
        self.entry_llegada.grid(row=2, column=1, padx=5, pady=5)

        # Botón para agregar el trabajo a la lista de preparación
        btn_agregar = tk.Button(frame_ingreso, text="Agregar a Lista", font=self.fuente_texto, 
                                bg=self.VERDE_PASTEL, relief="flat", command=self.agregar_tarea_lista)
        btn_agregar.grid(row=1, column=2, padx=15, rowspan=2)

        
        tk.Label(self.root, text="Trabajos programados para la simulación:", font=self.fuente_texto, bg="#F2F4F4").pack(anchor="w", padx=15, pady=(10, 2))
        
        self.listbox_tareas = tk.Listbox(self.root, font=("Courier New", 10), height=6)
        self.listbox_tareas.pack(fill="x", padx=15)

        
        frame_control = tk.Frame(self.root, bg="#F2F4F4")
        frame_control.pack(fill="x", padx=15, pady=15)

        tk.Label(frame_control, text="Velocidad Impresora (PPM):", font=self.fuente_texto, bg="#F2F4F4").pack(side="left")
        self.entry_ppm = tk.Entry(frame_control, font=self.fuente_texto, width=5)
        self.entry_ppm.insert(0, "12") 
        self.entry_ppm.pack(side="left", padx=5)

        btn_simular = tk.Button(frame_control, text="▶ Correr Simulación", font=self.fuente_texto, 
                                bg=self.AZUL_PASTEL, relief="flat", padx=10, command=self.ejecutar_simulacion)
        btn_simular.pack(side="right", padx=5)

        
        frame_resultados = tk.LabelFrame(self.root, text=" Reporte de Métricas Finales ", 
                                         font=self.fuente_texto, bg="#F2F4F4", fg="#162330", padx=10, pady=10)
        frame_resultados.pack(fill="both", expand=True, padx=15, pady=10)

        self.txt_reporte = tk.Text(frame_resultados, font=("Consolas", 11), bg="white", relief="flat")
        self.txt_reporte.pack(fill="both", expand=True)
        self.txt_reporte.config(state="disabled")

    def agregar_tarea_lista(self):
        
        id_doc = self.entry_id.get().strip()
        paginas_str = self.entry_paginas.get().strip()
        llegada_str = self.entry_llegada.get().strip()

        if not id_doc or not paginas_str or not llegada_str:
            messagebox.showwarning("Campos Vacíos", "Por favor, llene todos los datos del trabajo.")
            return

        try:
            paginas = int(paginas_str)
            llegada = int(llegada_str)

            # Validar estados inconsistentes o valores negativos
            if paginas <= 0 or llegada < 0:
                messagebox.showerror("Valor Inválido", "Las páginas deben ser mayores a 0 y el segundo no puede ser negativo.")
                return

            
            nueva_tarea = PrintTask(id_doc, paginas, llegada)
            self.lista_tareas_creadas.append(nueva_tarea)

            # Mostrar en la lista de la interfaz
            self.listbox_tareas.insert(tk.END, f"ID: {id_doc} | Páginas: {paginas} | Llega en seg: {llegada}")
            
            # me toca limpiar los campos para el siguiente ingreso
            self.entry_id.delete(0, tk.END)
            self.entry_paginas.delete(0, tk.END)
            self.entry_llegada.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Error de Formato", "Páginas y Segundo de Llegada deben ser números enteros.")

    def ejecutar_simulacion(self):
        
        if not self.lista_tareas_creadas:
            messagebox.showinfo("Simulación Vacía", "No hay trabajos en la lista para procesar.")
            return

        try:
            ppm = int(self.entry_ppm.get().strip())
            if ppm <= 0:
                messagebox.showerror("Error", "Las Páginas Por Minuto deben ser mayores a 0.")
                return
        except ValueError:
            messagebox.showerror("Error", "La velocidad PPM debe ser un número entero.")
            return

        # Me estada dando negativo, tons lo ordenamos la lista para que los que llegan primero se procesen primero
        self.lista_tareas_creadas.sort(key=lambda t: t.arrival_time)

        simulador = Simulation(ppm)

        
        primer_segundo = self.lista_tareas_creadas[0].arrival_time
        ultimo_segundo_llegada = max(t.arrival_time for t in self.lista_tareas_creadas)
        tiempo_total_estimado = ultimo_segundo_llegada + 1000 

        # El reloj empieza desde que llega el primer trabajo
        for segundo_actual in range(primer_segundo, tiempo_total_estimado):
            for tarea in list(self.lista_tareas_creadas):
                if tarea.arrival_time == segundo_actual:
                    simulador.add_task_to_simulation(tarea)
                    self.lista_tareas_creadas.remove(tarea) 
            
            simulador.run_simulation_step(segundo_actual)

        
        resultados = simulador.get_metrics()

        # Mostrar los resultados en el cuadro de texto
        self.txt_reporte.config(state="normal")
        self.txt_reporte.delete("1.0", tk.END)
        
        reporte_formato = (
            f"          RESULTADOS DE LA SIMULACIÓN       \n"
            f" * Trabajos totales procesados: {resultados['total']}\n"
            f" * Tamaño máximo alcanzado por la cola: {resultados['max_cola']}\n"
            f" * Tiempo promedio de espera en cola: {resultados['promedio_espera']} seg.\n"
            f" * Trabajo con mayor tiempo de espera: '{resultados['max_espera_id']}'\n"
            f"   (Esperó un total de: {resultados['max_espera_tiempo']} segundos)\n\n"
            f" ------------------------------------------\n"
            f" Estado del sistema: Simulación finalizada.\n"
        )
        
        self.txt_reporte.insert(tk.END, reporte_formato)
        self.txt_reporte.config(state="disabled")
        
        # Limpiar la lista de la interfaz tras terminar 
        self.lista_tareas_creadas.clear()
        self.listbox_tareas.delete(0, tk.END)

    def reiniciar_simulacion(self):
        """Borra todos los datos guardados y limpia los componentes de la interfaz."""
        # Limpiar las variables de memoria
        self.lista_tareas_creadas.clear()
        
        # Limpiar los campos de texto de entrada
        self.entry_id.delete(0, tk.END)
        self.entry_paginas.delete(0, tk.END)
        self.entry_llegada.delete(0, tk.END)
        
        # Reestablecer las PPM al valor por defecto
        self.entry_ppm.insert(0, "12")
        self.entry_ppm.delete(0, tk.END)
        
        # Vaciar la lista visual de trabajos
        self.listbox_tareas.delete(0, tk.END)
        
        # 4. Limpiar el cuadro del reporte de métricas
        self.txt_reporte.config(state="normal")
        self.txt_reporte.delete("1.0", tk.END)
        self.txt_reporte.config(state="disabled")
        
        # Mensaje opcional de un aviso silencioso
        messagebox.showinfo("Reiniciar", "El simulador se ha limpiado y está listo para nuevos trabajos.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImpresoraGUI(root)
    root.mainloop()