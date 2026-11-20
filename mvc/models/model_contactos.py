from supabase import create_client, Client
from dotenv import load_dotenv
import os
import hashlib
import hmac
import logging

load_dotenv()
logger = logging.getLogger(__name__)


class ModelContactos:
    def __init__(self) -> None:
        self.SECRET_KEY = os.environ.get("SECRET_KEY", "12345678").encode("utf-8")
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL", ""),
                os.environ.get("SUPABASE_KEY", "")
            )
        except Exception as error:
            logger.error(f"Error 100: {str(error)}")
            print(f"ERROR 100: {error.args[0]}")

    def generar_hash(self, id: int) -> str:
        """Devuelve un hash HMAC-MD5 de 32 caracteres hex a partir del ID."""
        try:
            return hmac.new(
                self.SECRET_KEY, str(id).encode("utf-8"), hashlib.md5
            ).hexdigest()
        except Exception as error:
            print(f"ERROR 106: {str(error)}")
            return ""

    def validar_hash(self, hash_a_validar: str) -> int | None:
        """Busca el id real cuyo hash coincide. None si no existe."""
        try:
            if not hash_a_validar or len(hash_a_validar) != 32:
                return None
            response = self.supabase.table("contactos").select("id_contacto").execute()
            for fila in response.data:
                esperado = self.generar_hash(fila["id_contacto"])
                if hmac.compare_digest(esperado, hash_a_validar):
                    return fila["id_contacto"]
            return None
        except Exception as error:
            print(f"ERROR 107: {str(error)}")
            return None

    def obtenerContactos(self) -> list:
        try:
            response = self.supabase.table("contactos").select("*").execute()
            contactos = response.data
            for c in contactos:
                c["hash"] = self.generar_hash(c["id_contacto"])
                del c["id_contacto"]  # el id real ya no sale a la vista
            return contactos
        except Exception as error:
            logger.error(f"Error 101: {str(error)}")
            print(f"ERROR 101: {error.args[0]}")
            return []

    def buscarContacto(self, hash_contacto: str):
        try:
            id_contacto = self.validar_hash(hash_contacto)
            if id_contacto is None:
                return []
            response = self.supabase.table("contactos").select("*").eq("id_contacto", id_contacto).execute()
            contactos = response.data
            for c in contactos:
                c["hash"] = self.generar_hash(c["id_contacto"])
                del c["id_contacto"]
            return contactos
        except Exception as error:
            logger.error(f"Error 102: {str(error)}")
            print(f"ERROR 102: {error.args[0]}")
            return []

    def insertarContacto(self, nombre: str, telefono: str, email: str, foto:str):
        try:
            data = {"nombre": nombre, "telefono": telefono, "email": email,"foto":foto}
            response = self.supabase.table("contactos").insert(data).execute()
            return response.data
        except Exception as error:
            logger.error(f"Error 103: {str(error)}")
            print(f"ERROR 103: {error.args[0]}")

    def borrarContacto(self, hash_contacto: str):
        try:
            id_contacto = self.validar_hash(hash_contacto)
            if id_contacto is None:
                return None
            response = self.supabase.table("contactos").delete().eq("id_contacto", id_contacto).execute()
            return response.data
        except Exception as error:
            logger.error(f"Error 104: {str(error)}")
            print(f"ERROR 104: {error.args[0]}")

    def actualizarContacto(self, hash_contacto: str, nombre: str, telefono: str, email: str, foto:str):
        try:
            id_contacto = self.validar_hash(hash_contacto)
            if id_contacto is None:
                return None
            data = {"nombre": nombre, "telefono": telefono, "email": email,"foto":foto}
            response = self.supabase.table("contactos").update(data).eq("id_contacto", id_contacto).execute()
            return response.data
        except Exception as error:
            logger.error(f"Error 105: {str(error)}")
            print(f"ERROR 105: {error.args[0]}")

if __name__=="__main__":
    model_contactos = ModelContactos()
    #print(model_contactos.obtenerContactos())
    #print(model_contactos.buscarContacto(15))
    print(model_contactos.insertarContacto("josue","7777777777","josue@email.com","default.png"))
    #print(model_contactos.borrarContacto(2))
    #print(model_contactos.actualizarContacto(1,"hola","8888888888","hola@email.com"))