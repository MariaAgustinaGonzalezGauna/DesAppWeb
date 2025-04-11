# Arquitectura de 3 Capas - Aplicación de Productos

## 📁 Estructura del Proyecto

- `app.py`: Capa de Presentación.
  - Define las rutas `/agregar` y `/productos`.
  - Recibe peticiones del usuario y delega el trabajo a la capa de negocio.

- `negocio.py`: Capa de Lógica de Negocio.
  - Procesa los datos y aplica las reglas del negocio.
  - Valida y transforma información si es necesario.
  - Comunica la capa de presentación con la de datos.

- `datos.py`: Capa de Acceso a Datos.
  - Simula una base de datos usando una lista en memoria.
  - Encapsula toda la lógica de almacenamiento y recuperación de productos.

## ✅ Ventajas respecto a la versión monolítica

- **Mejor organización**: Cada archivo tiene una responsabilidad clara.
- **Escalabilidad**: Podemos crecer la app sin que todo esté mezclado en un solo archivo.
- **Fácil de mantener**: Cambios en una capa no afectan a las otras directamente.
- **Testing más sencillo**: Podemos probar cada módulo por separado.
- **Reutilización**: Las funciones en la capa de negocio y datos pueden ser usadas por otras interfaces (ej. API REST, CLI, GUI).

