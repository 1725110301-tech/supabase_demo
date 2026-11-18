from supabase import create_client, Client
from dotenv import load_dotenv
import os
import hashlib
import hmac

import logging


load_dotenv()
logger=logging.getLogger(__name__)

class ModelContactos:
    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL", ""),
                os.environ.get("SUPABASE_KEY", "")
            )
        except Exception as error:
            logger.error(f"Error 100: {str(error)}")
            print(f"ERROR 100: {error.args[0]}")


    def generar_hash(self,id: int) -> str:
        try:
            """Genera un hash único a partir del ID."""
            mensaje = str(id).encode("utf-8")
            firma =  hmac.new(self.SECRET_KEY, mensaje, hashlib.sha256).hexdigest()
            # Concatena el id:firma
            return f"{id}:{firma}"
        except Exception as error:
            print(f"ERROR 106: {str(error)}")
            return ""


    def validar_hash(self,hash_a_validar: str) -> int|None:
        try:
            # Separa el id, separador y la firma
            id_str, sep, _ = hash_a_validar.partition(":")
            resultado_id = None

            # Solo calculamos el hash si la estructura básica es válida
            if sep and id_str.isdigit():
                token_esperado = self.generar_hash(int(id_str))
                if hmac.compare_digest(token_esperado, hash_a_validar):
                    resultado_id = int(id_str)
                else:
                    resultado_id = None
            else:
                resultado_id = None

            return resultado_id
        except Exception as error:
            print(f"ERROR 107: {str(error)}")
            return -1

    def obtenerContactos(self)-> None:
        try:
            response = self.supabase.table("contactos").select("*").execute()
            return response.data
        except Exception as error:
            logger.error(f"Error 101: {str(error)}")
            print(f"ERROR 101: {error.args[0]}")
    
    def buscarContacto(self, id_contacto:int):
        try:
            response = self.supabase.table("contactos").select("*").eq("id_contacto", id_contacto).execute()
            return response.data
        except Exception as error:
            logger.error(f"Error 102: {str(error)}")
            print(f"ERROR 102: {error.args[0]}")

    def insertarContacto(self,nombre:str,telefono:str,email:str):
        try:
            data={
                "nombre":nombre,
                "telefono":telefono,
                "email":email
            }
            response = self.supabase.table("contactos").insert(data).execute()
            return response.data
        except Exception as error:
            logger.error(f"Error 103: {str(error)}")
            print(f"ERROR 103: {error.args[0]}")

    def borrarContacto(self,id_contacto:int):
        try:
            response = self.supabase.table("contactos").delete().eq("id_contacto", id_contacto).execute()
            return response.data
        except Exception as error:
            logger.error(f"Error 104: {str(error)}")
            print(f"ERROR 104: {error.args[0]}")
    def actualizarContacto(self, id_contacto: int, nombre: str, telefono: str, email: str):

        try:
            data = {
                "nombre": nombre,
                "telefono": telefono,
                "email": email
            }
            response = self.supabase.table("contactos").update(data).eq("id_contacto", id_contacto).execute()
            return response.data
        except Exception as error:
            logger.error(f"Error 105: {str(error)}")
            print(f"ERROR 105: {error.args[0]}")


if __name__=="__main__":
    model_contactos = ModelContactos()
    #print(model_contactos.obtenerContactos())
    #print(model_contactos.buscarContacto(15))
    #print(model_contactos.insertarContacto("josue","7777777777","josue@email.com"))
    #print(model_contactos.borrarContacto(2))
    #print(model_contactos.actualizarContacto(1,"hola","8888888888","hola@email.com"))