import sys
import time

def process_massive_data_stream(data_source):
    """
    Simula un flujo de datos (ej. 1 millón de registros de una DB o CSV).
    Usa un Generador para mantener un uso de memoria cercano a 0.
    """
    for i in range(1000000):
        yield f"student_record_{i % 50000}"  # Genera duplicados intencionales

def filter_unique_records(stream):
    """
    Filtra duplicados usando un Set para búsqueda O(1).
    """
    seen = set()
    unique_count = 0
    
    print(f"[*] Iniciando procesamiento...")
    start_time = time.time()

    for record in stream:
        if record not in seen:
            seen.add(record)
            unique_count += 1
            # Aquí se escribiría en la DB o S3
    
    end_time = time.time()
    
    print(f"[✓] Procesamiento completado en: {end_time - start_time:.4f} seg")
    print(f"[✓] Registros únicos encontrados: {unique_count}")
    print(f"[✓] Uso de memoria del Set: {sys.getsizeof(seen) / 1024 / 1024:.2f} MB")

if __name__ == "__main__":
    # Ejecutamos la lógica
    data_stream = process_massive_data_stream(None)
    filter_unique_records(data_stream)
