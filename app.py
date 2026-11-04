from supabase import create_client, Client
from dotenv import load_dotenv
import os
load_dotenv()


class ModelContactos:
    def __init__(self) -> None:
        try:
            supabase: Client = create_client(
                os.environ.get("SUPABASE_URL", ""),
                os.environ.get("SUPABASE_KEY", "")
            )
        except Exception as error:
            print(f"ERROR 100: {error.args[0]}")



def obtenerContactos(self)-> None:

    response = supabase.table("contactos").select("*").execute()
    return response.data


model_contactos = ModelContactos()
print(obtenerContactos())