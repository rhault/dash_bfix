import os
from urllib.parse import urlparse
from dotenv import load_dotenv
import psycopg2

load_dotenv()

db_url = urlparse(os.getenv("DATABASE_URL"))
conn = None


def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname=db_url.path[1:],
            user=db_url.username,
            password=db_url.password,
            host=db_url.hostname,
            port=db_url.port,
        )

        cur = conn.cursor()
        cur.execute("SELECT version();")
        db_version = cur.fetchone()
        print(f"Connected to PostgreSQL', ${db_version}")
        cur.close()

    except psycopg2.Error as err:
        print(f"Error connecting to PostgreSQL: ${err}")

    finally:
        if conn:
            conn.close()
