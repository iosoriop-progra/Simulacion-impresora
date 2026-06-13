from cola import Queue, PrintTask

class Printer:
    def __init__(self, pages_per_minute):
        self.ppm = pages_per_minute     
        self.current_task = None        
        self.time_remaining = 0  




    def is_busy(self):
        # Si hay tiempo restante, dejen chambear 
        return self.current_task is not None
    




    def start_next(self, new_task):
        self.current_task = new_task
        
        self.time_remaining = int((new_task.pages / self.ppm) * 60)

    def tick(self):
        #pa que avance un tiempo la impresora 
        if self.is_busy():
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None


class Simulation:
    def __init__(self, ppm):
        self.printer = Printer(ppm)
        self.queue = Queue()
        self.completed_tasks = []
        self.max_queue_size = 0
        self.waiting_times = []
        self.max_waiting_time = 0
        self.task_with_max_wait = None

    def add_task_to_simulation(self, task):
        # para que se puedan meter, hay que validar  
        if task.pages <= 0:
            return False, "Error: Las páginas deben ser mayores a 0."
        
        self.queue.enqueue(task)
        # vamos viendo si la cola alcanzó un nuevo tamaño máximo
        if self.queue.size() > self.max_queue_size:
            self.max_queue_size = self.queue.size()
        return True, "Trabajo en cola."

    def run_simulation_step(self, current_second):
        """Este método simula lo que pasa en un segundo específico."""
        # Si la impresora está libre y hay algo en la cola, toma el siguiente
        if not self.printer.is_busy() and not self.queue.is_empty():
            next_task = self.queue.dequeue()
            
            # Calculamos cuánto tiempo esperó en la cola (las colas, siempre las colas)
            wait_time = current_second - next_task.arrival_time
            self.waiting_times.append(wait_time)
            
            
            if wait_time > self.max_waiting_time:
                self.max_waiting_time = wait_time
                self.task_with_max_wait = next_task.task_id

            self.printer.start_next(next_task)
            self.completed_tasks.append(next_task)

        
        self.printer.tick()

    def get_metrics(self):
        """Calcula y devuelve los resultados finales."""
        total_processed = len(self.completed_tasks)
        
        # Validación por si se corre una simulación sin trabajos
        if total_processed == 0:
            return {
                "total": 0,
                "promedio_espera": 0,
                "max_espera_tiempo": 0,
                "max_espera_id": "Ninguno",
                "max_cola": self.max_queue_size
            }
        
        promedio = sum(self.waiting_times) / total_processed
        
        return {
            "total": total_processed,
            "promedio_espera": round(promedio, 2),
            "max_espera_tiempo": self.max_waiting_time,
            "max_espera_id": self.task_with_max_wait if self.task_with_max_wait else "Ninguno",
            "max_cola": self.max_queue_size
        }


#vamos con otras pruebas solicitadas
def probar_simulacion():
    print("Corriendo pruebas de impresora.py...")
    
    sim = Simulation(ppm=10) # 10 páginas por minuto
    
    
    tarea_mala = PrintTask("DocInvalido", 0, 0)
    exito, msg = sim.add_task_to_simulation(tarea_mala)
    assert exito == False
    
    
    t1 = PrintTask("Doc1", 5, 0) # Debería tardar 30 segundos
    sim.add_task_to_simulation(t1)
    
    
    sim.run_simulation_step(0)
    assert sim.printer.is_busy() == True
    
    metrics = sim.get_metrics()
    assert metrics["total"] == 1
    assert metrics["max_cola"] == 1
    
    print("Pruebas de procesamiento y simulación pasadas con éxito.")

if __name__ == "__main__":
    probar_simulacion()