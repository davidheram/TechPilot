import json 
import os

RUTA_MEMORIA = "data/conversaciones.json"

def cargar_historial():
    if os.path.exists(RUTA_MEMORIA):
        try: 
            with open(RUTA_MEMORIA, "r", encoding="utf-8-sig") as f: 
                contenido = f.read()
                if contenido.strip():
                    return json.loads(contenido)
        except:        
            return []

    return []    

def guardar_historial(historial): 
    with open(RUTA_MEMORIA, "w", encoding="utf-8-sig") as f: 
        json.dump(historial, f, ensure_ascii=True, indent=2)