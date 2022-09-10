import mysql.connector
from dotenv import load_dotenv
from os import getenv

load_dotenv()
server = mysql.connector.connect(host=getenv("DBHOST"), user=getenv("DBUSER"), password=getenv("DBPASSWORD"), database=getenv("DBNAME"), autocommit=True)
cursor = server.cursor(buffered=True)

def checkTableExists(dbcon, tablename):
    dbcur = dbcon.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True

    dbcur.close()
    return False

if checkTableExists(server, "ideas"):
    pass
else:
    cursor.execute(f"""
        CREATE TABLE ideas(

        email VARCHAR(255),
        name VARCHAR(250),
        word VARCHAR(255),
        wordpro VARCHAR(260),
        wordmening VARCHAR(655)
    )
        """)


def insert(email, name, word, wordpro, wordmening):
    
    email = str(email).replace('"', '\\"')
    name = str(name).replace('"', '\\"')
    word = str(word).replace('"', '\\"')
    wordpro = str(wordpro).replace('"', '\\"')
    wordmening = str(wordmening).replace('"', '\\"')

    cursor.execute(f"""
    INSERT INTO ideas VALUES("{email}", "{name}", "{word}", "{wordpro}", "{wordmening}");
    """)

def getAll():
    cursor.execute(f"""
    SELECT * FROM ideas;
    """)
    results = ""
    for a in cursor.fetchall():
        results = results + str(a) + "<br>"

    return results

def DeleteAll():
    cursor.execute("""
    DELETE FROM ideas;
    """)