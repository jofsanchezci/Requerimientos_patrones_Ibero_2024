
# Ejemplo de Patrón Singleton con SQLite en Python

Este proyecto es un ejemplo de cómo implementar el **Patrón Singleton** en Python utilizando una conexión a una base de datos **SQLite**. El patrón Singleton asegura que solo se cree una única instancia de la conexión, lo cual es útil para optimizar el uso de recursos, especialmente en sistemas escalables.

## Descripción

El objetivo principal de este ejemplo es mostrar cómo utilizar el patrón Singleton para manejar conexiones a una base de datos SQLite de manera eficiente. Este patrón es ideal cuando solo se necesita una conexión a un recurso compartido (como una base de datos) a lo largo del ciclo de vida de la aplicación.

### Estructura del Código

El código está estructurado en la clase `DatabaseConnection`, que gestiona la creación y uso de la conexión a la base de datos.

- **`__new__()`**: Controla la creación de la instancia Singleton.
- **`_create_connection(db_name)`**: Establece una conexión con la base de datos SQLite.
- **`get_connection()`**: Retorna la conexión actual.
- **`close_connection()`**: Cierra la conexión a la base de datos.

## Código de Ejemplo

```python
import sqlite3

class DatabaseConnection:
    _instance = None  # Variable de clase para almacenar la instancia única

    def __new__(cls, db_name):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance.connection = cls._create_connection(db_name)
        return cls._instance

    @staticmethod
    def _create_connection(db_name):
        try:
            # Crea una conexión a la base de datos SQLite
            connection = sqlite3.connect(db_name)
            print(f"Conexión a {db_name} establecida.")
            return connection
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None

    def get_connection(self):
        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")


# Ejemplo de uso
if __name__ == "__main__":
    # Se crea la primera instancia de la conexión a la base de datos 'example.db'
    db1 = DatabaseConnection('example.db')
    conn1 = db1.get_connection()

    # Intenta crear otra instancia de conexión a 'example.db', pero es la misma instancia
    db2 = DatabaseConnection('example.db')
    conn2 = db2.get_connection()

    # Verificar que ambas instancias son iguales (misma conexión)
    print(db1 is db2)  # Salida: True

    # Cerrar la conexión
    db1.close_connection()
```

## Ejecución

Para ejecutar este código, simplemente sigue estos pasos:

1. Asegúrate de tener Python instalado en tu sistema.
2. Descarga o clona este repositorio.
3. Ejecuta el archivo `singleton_sqlite.py` desde la línea de comandos:

```bash
python singleton_sqlite.py
```

## Conclusión

Este ejemplo demuestra cómo el patrón Singleton puede ser útil para gestionar conexiones a bases de datos y otros recursos compartidos en aplicaciones escalables. En este caso, la implementación asegura que solo exista una única instancia de la conexión a la base de datos **SQLite**, evitando la sobrecarga de recursos innecesarios.

