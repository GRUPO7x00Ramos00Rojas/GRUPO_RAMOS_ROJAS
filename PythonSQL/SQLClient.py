import psycopg2

class Database:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            # Establecer conexión
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )

            # Crear cursor
            self.cursor = self.connection.cursor()

        except (Exception, psycopg2.Error) as error:
            print("Error al conectar con PostgreSQL", error)

    def execute_query(self):
        if not self.cursor:
            print("No hay conexión a la base de datos. Por favor, conecta primero.")
            return

        # Solicitar consulta por pantalla
        query = input("Por favor, introduce tu consulta SQL: ")

        # Ejecutar consulta
        self.cursor.execute(query)

        # Obtener y mostrar los resultados
        records = self.cursor.fetchall()
        for record in records:
            print(record)

    def close(self):
        # Cerrar la conexión y el cursor
        if self.connection:
            self.cursor.close()
            self.connection.close()

# Crear un objeto de la clase Database y realizar operaciones en la base de datos
db = Database("192.168.1.104", "5432", "postgres", "postgres", "Admin.123")
db.connect()
db.execute_query()
db.close()
