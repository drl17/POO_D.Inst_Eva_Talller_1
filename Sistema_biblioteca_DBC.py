import pyodbc
from tabulate import tabulate

# Especifica los detalles de la conexión
server = 'DESKTOP-V8L2OJS\\SQLEXPRESS'
database = 'Sistema_biblioteca'
trusted_connection = 'yes'
driver = '{SQL Server}'

# Crea la cadena de conexión
connection_string = f'SERVER={server};DATABASE={database};TRUSTED_CONNECTION={trusted_connection};DRIVER={driver}'

try:
    # Establece la conexión
    conn = pyodbc.connect(connection_string)

    # Crea un cursor para ejecutar consultas
    cursor = conn.cursor()

    # Ejemplo de consulta
    cursor.execute("SELECT @@version AS version")
    row = cursor.fetchone()

    # Imprime el resultado
    while row:
        print(row.version)
        row = cursor.fetchone()

except pyodbc.Error as ex:
    print(f"Error: {ex}")

with conn.cursor() as cursor:
    cursor.execute("select Title, Author, Year_publishment, isbn, stock from Books")

    da = cursor.fetchall()
    print(tabulate(da, headers=['Title', 'Author', 'Year_publishment', 'isbn', 'stock'], tablefmt="grid"))

conn.close()

# Insertar nuevo libro en la biblioteca
# Preguntar al usuario para hacer actualización de libros

class Product:
    def __init__(self, Title, Author, Year_publishment, isbn, stock):
        self.Title = Title
        self.Author = Author
        self.Year_publishment = Year_publishment
        self.isbn = isbn
        self.stock = stock

def inG_Product():
    print("Bienvenido al sistema biblioteca. Aquí procederá a actualizar la lista de libros existentes.")
    print()

    Title = input("Ingrese el título del libro: ")
    Author = input("Ingrese el nombre del autor: ")
    Year_publishment = int(input("Ingrese el año de publicación del libro: "))
    isbn = int(input("Ingrese el código ISBN: "))
    stock = int(input("Ingrese la cantidad de estos libros a ingresar:"))

    return Product(Title, Author, Year_publishment, isbn, stock)

def insertProduct(product, connection_string):
    connection = pyodbc.connect(connection_string)

    try:
        cursor = connection.cursor()

        insert_query = """INSERT INTO Books (Title, Author, Year_publishment, isbn, stock) 
        VALUES (?, ?, ?, ?, ?)"""

        product_data = (
            product.Title,
            product.Author,
            product.Year_publishment,
            product.isbn,
            product.stock
        )

        cursor.execute(insert_query, product_data)
        connection.commit()
        print("Datos Guardados!!!")

    except pyodbc.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        connection.close()

new_product = inG_Product()
db_connection_instance = f'SERVER={server};DATABASE={database};TRUSTED_CONNECTION={trusted_connection};DRIVER={driver}'
insertProduct(new_product, db_connection_instance)
