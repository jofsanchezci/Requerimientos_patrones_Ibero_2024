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
