# Performance Optimization Lab (Python) 🐍
Este repositorio contiene una **Prueba de Concepto (PoC)** sobre cómo manejar la desduplicación de datos en sistemas de alta escala.

Este repositorio contiene una Prueba de Concepto (PoC) sobre cómo manejar la desduplicación de datos en sistemas de alta escala (como el ERP Académico mencionado en mi CV).

Conceptos aplicados: 
  - Generators (Lazy Evaluation): Evito cargar millones de registros en RAM, procesando el flujo uno a uno.
  - Sets para Memoria Eficiente: Utilizo tablas hash internas de Python para asegurar búsquedas de duplicados en tiempo constante $O(1)$.
  - Scalability: Esta lógica es la base para procesos asíncronos en Celery que manejé profesionalmente.
