class Queue:
    def __init__(self):
        # Se debe crear una lista para poder guardar los trabajos :,(
        self.__items = []

    def enqueue(self, item):
        # Agrega un elemento al final de la cola
        self.__items.append(item)

    def dequeue(self):
        # Esta funcion se creó para remover y devuelver el primer elemento (el del inicio)
        if self.is_empty():
            return None
        return self.__items.pop(0)

    def peek(self):
        # para no olvidarlo, aqui se mira el primer elemento sin sacarlo de la cola
        if self.is_empty():
            return None
        return self.__items[0]

    def is_empty(self):
        return len(self.__items) == 0

    def size(self):
        return len(self.__items)


class PrintTask:
    def __init__(self, task_id, pages, arrival_time):
        self.task_id = task_id          
        self.pages = pages             
        self.arrival_time = arrival_time  


#toca el turno de las prubeas mínimas 
def probar_cola():
    print("Corriendo pruebas de cola.py...")
    
    # Probar que la cola funcione FIFO
    q = Queue()
    assert q.is_empty() == True
    
    t1 = PrintTask("Doc1", 5, 0)
    t2 = PrintTask("Doc2", 10, 2)
    
    q.enqueue(t1)
    q.enqueue(t2)
    
    assert q.size() == 2
    assert q.peek().task_id == "Doc1"
    
    # Aqui se valida si el que salio primero es el que entro 
    atendido = q.dequeue()
    assert atendido.task_id == "Doc1"
    assert q.size() == 1
    
    print("Pruebas de cola y tareas pasadas con éxito.")

if __name__ == "__main__":
    probar_cola()