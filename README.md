Simulador de cola de impresión basado en estructuras fifo
Este proyecto consiste en una aplicación desarrollada en python que simula un entorno de impresión real mediante el uso de colas. 
El sistema permite modelar el flujo de trabajo en una oficina o centro de cómputo donde múltiples usuarios envían documentos de distintas longitudes en diferentes momentos, 
obligando al sistema a organizar los archivos en una fila de espera organizada bajo el principio de que el primer elemento en llegar es el primero en ser atendido de forma obligatoria.

La importancia del proyecto radica en la implementación y el análisis de los tipos de datos abstractos aplicados a la resolución de problemas de logística. El software no solo gestiona el almacenamiento temporal de las tareas, sino que también actúa como un motor de analítica que mide el rendimiento del equipo de impresión, calculando tiempos exactos de retraso para determinar si la velocidad configurada es óptima para la demanda del entorno simulado.

Características principales del sistema
El simulador cumple con una serie de requerimientos técnicos y arquitectónicos que garantizan su correcto funcionamiento y su facilidad de uso a través de componentes visuales.

Estructura de datos propia: La cola utilizada para gestionar los trabajos fue programada desde cero, encapsulando una lista interna para prohibir alteraciones externas y obligar al sistema a interactuar únicamente a través de los métodos formales de inserción y extracción.

Motor lógico temporal: La simulación no utiliza funciones de pausa reales que alentarían la ejecución, sino que emplea un bucle abstracto que procesa el tiempo segundo a segundo de manera instantánea, agilizando el cálculo de métricas complejas.

Validación de datos interactiva: El sistema cuenta con capas de seguridad que interceptan los datos ingresados por el usuario, rechazando cantidades de páginas menores a una o tiempos de llegada negativos para prevenir estados inconsistentes en la memoria.

Interfaz amigable: El entorno visual delega la consola para ofrecer un diseño limpio en colores pastel, facilitando la lectura de la lista de tareas programadas y protegiendo el cuadro de resultados contra escrituras accidentales.

Arquitectura de módulos
El código fuente se encuentra dividido de forma estricta en tres archivos independientes para respetar los lineamientos de separación de la lógica de negocio y la interfaz de usuario.

Módulo de la cola: Este archivo resguarda la clase de la cola con sus operaciones de consulta, inserción y tamaño, además de la clase que define los atributos del trabajo de impresión como su identificación, páginas y segundo de arribo.

Módulo de la impresora: Este componente contiene la clase de la impresora que controla el estado operativo de la máquina y el tiempo restante de los archivos, y la clase de simulación que gestiona el reloj y las variables estadísticas.

Módulo de la interfaz: Este bloque final maneja la ventana principal, los campos de captura de datos, los botones de ejecución o reinicio, y se comunica con el motor lógico para plasmar los resultados finales en la pantalla.

Métricas de rendimiento reportadas
Al concluir el procesamiento de todas las tareas, la aplicación recopila los datos temporales guardados en el motor y despliega de manera automática un informe con indicadores clave.

Total de trabajos procesados: Contabiliza de forma exacta el volumen de documentos que completaron su ciclo de impresión con éxito.

Tamaño máximo de la cola: Registra el punto más crítico de saturación del sistema, indicando la mayor cantidad de archivos que hicieron fila de manera simultánea.

Tiempo promedio de espera: Aplica una fórmula matemática para promediar la cantidad de segundos que los trabajos permanecieron retenidos antes de pasar a la impresora.

Documento con mayor retraso: Identifica el nombre específico del archivo que experimentó la espera más larga junto con su tiempo exacto en segundos.

Guía de uso y ejecución
Para poner en marcha la aplicación es necesario contar con el intérprete de python instalado y ubicar los tres archivos dentro del mismo directorio de trabajo. El programa se inicia ejecutando el archivo principal desde la terminal de comandos, lo que desplegará de inmediato la interfaz gráfica en la pantalla. Una vez abierta la ventana, el usuario puede registrar múltiples trabajos ingresando sus datos en los campos correspondientes y presionando el botón de agregar a la lista.

Una vez que se han programado todos los documentos deseados, se define la velocidad de la máquina en páginas por minuto y se pulsa el botón de correr simulación para generar el reporte de métricas al instante. Si se desea realizar una nueva prueba con diferentes parámetros, el botón de reiniciar borrará todas las variables de la memoria y limpiará la pantalla de forma segura para comenzar desde cero.
