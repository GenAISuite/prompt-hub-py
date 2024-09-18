import psycopg2
import os

class DBConfig:
    def __init__(self):
        self.db_config = {
             'dbname': os.environ.get('DATABASE_NAME', 'prompt_hub'),
        'user': os.environ.get('DATABASE_USER', 'postgres'),
        'password': os.environ.get('DATABASE_PASSWORD', 'postgres'),
        'host': os.environ.get('DATABASE_HOST', 'localhost'),
        'port': os.environ.get('DATABASE_PORT', '5432')
        }
        self.conn = None

    def connect(self):
        """Establish a connection to the PostgreSQL database."""
        if not self.conn:
            try:
                self.conn = psycopg2.connect(**self.db_config)
            except psycopg2.Error as e:
                print(f"Error connecting to the database: {e}")
                raise
        return self.conn

    def close(self):
        """Close the connection to the database."""
        if self.conn:
            self.conn.close()
            self.conn = None
    
    def run_query(self, name):
        """Run a query against the database."""
        result = None
        try:
            self.connect()
            query = "SELECT prompt FROM prompt WHERE name = %s"
            with self.conn.cursor() as cur:
                cur.execute(query, (name,))
                result = cur.fetchone()
                if result:
                    return result[0]
                else:
                    return None
        except Exception as e:
            print(f"Error running query: {e}")
            raise
        finally:
            self.close()

