class ConfiguraciónSimple:
    def __init__(self):
        self.modo_debug = False
        self.max_conexiones = 100
        self.tiempo_espera = 30
        
mi_config = ConfiguraciónSimple()

print("--- Configuración del Sistema ---")
print(f"Modo Debug: {mi_config.modo_debug}")
print(f"Máximo de conexiones: {mi_config.max_conexiones}")
print(f"Tiempo de espera: {mi_config.tiempo_espera} segundos")

# También puedes cambiar un valor después de crearla
mi_config.modo_debug = True
print(f"\nModo Debug actualizado: {mi_config.modo_debug}")