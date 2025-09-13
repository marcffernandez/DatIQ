"""
utils.py - Funciones auxiliares para conectar a la base de datos Supabase (PostgreSQL)
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from dotenv import load_dotenv
import pandas as pd

def get_engine() -> Engine:
    """
    Crea una conexión SQLAlchemy al PostgreSQL de Supabase usando la variable DATABASE_URL
    definida en el archivo .env.
    """
    load_dotenv()  # Carga las variables del archivo .env
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise ValueError("No se encontró DATABASE_URL en el archivo .env")

    engine = create_engine(database_url)
    return engine

def fetch_table(table_name: str, limit: int = 10) -> pd.DataFrame:
    """
    Devuelve un DataFrame con las primeras filas de la tabla solicitada.
    
    Args:
        table_name (str): Nombre de la tabla en la base de datos.
        limit (int): Número de filas a devolver (default: 10)
    
    Returns:
        pd.DataFrame con los datos de la tabla.
    """
    engine = get_engine()
    query = f"SELECT * FROM {table_name} LIMIT {limit};"
    df = pd.read_sql(query, engine)
    return df

if __name__ == "__main__":
    # Ejemplo de prueba: listar 5 clientes
    df_clientes = fetch_table("clientes", limit=5)
    print(df_clientes)
