from peewee import MySQLDatabase
from dotenv import load_dotenv
import os
import peewee

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Configuración de la base de datos MySQL utilizando las variables de entorno
database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE", "gestionusuarios"),  # Nombre de la base de datos
    user=os.getenv("MYSQL_USER", "root"),            # Usuario de MySQL
    password=os.getenv("MYSQL_PASSWORD", "root"),    # Contraseña de MySQL
    host=os.getenv("MYSQL_HOST", "localhost"),       # Host de MySQL
    port=int(os.getenv("MYSQL_PORT", 3306))          # Puerto de MySQL
)

def connect_db():
    """Conexion a la base de datos."""
    try:
        if database.is_closed():
            database.connect(reuse_if_open=True)
            print("✅ Conexión exitosa a la base de datos.")
    except peewee.OperationalError as e:
        print(f"❌ Error, no se pudo conectar a la base de datos: {e}")
    except Exception as e:
        print(f"❌ Error, no se pudo conectar a la base de datos: {e}")

def close_db():
    """Método para cerrar conexiones a la base de datos que estén abiertas."""
    try:
        if not database.is_closed():
            database.close()
            print("✅ Conexión Finalizada con éxito.")
    except peewee.OperationalError as e:
        print(f"❌ Error, no se pudo finalizar la conexión con la base de datos: {e}")
    except Exception as e:
        print(f"❌ Error, no se pudo finalizar la conexión con la base de datos: {e}")

def create_tables(models):
    """Método que permite crear las tablas en caso de que no existan en la base de datos."""
    try:
        with database:
            database.create_tables(models)
            print("✅ Las Tablas se han creado con éxito.")
    except peewee.OperationalError as e:
        print(f"❌ Error, no fue posible crear las tablas en la base de datos: {e}")
    except Exception as e:
        print(f"❌ Error, no fue posible crear las tablas en la base de datos: {e}")
