from supabase import create_client, Client
from dotenv import load_dotenv
import os
load_dotenv()


class ModelContactos:
    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL", ""),
                os.environ.get("SUPABASE_KEY", "")
            )
        except Exception as error:
            print(f"ERROR 100: {error.args[0]}")



    def obtenerContactos(self)-> None:
        try:
            response = self.supabase.table("contactos").select("*").execute()
            return response.data
        except Exception as error:
            print(f"ERROR 101: {error.args[0]}")
    
    def buscarContacto(self, id_contacto:int):
        try:
            response = self.supabase.table("contactos").select("*").eq("id_contacto", id_contacto).execute()
            return response.data
        except Exception as error:
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
            print(f"ERROR 103: {error.args[0]}")

    def borrarContacto(self,id_contacto:int):
        try:
            response = self.supabase.table("contactos").delete().eq("id_contacto", id_contacto).execute()
            return response.data
        except Exception as error:
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
            print(f"ERROR 105: {error.args[0]}")


if __name__=="__main__":
    model_contactos = ModelContactos()
    #print(model_contactos.obtenerContactos())
    #print(model_contactos.buscarContacto(15))
    #print(model_contactos.insertarContacto("josue","7777777777","josue@email.com"))
    #print(model_contactos.borrarContacto(2))
    #print(model_contactos.actualizarContacto(1,"hola","8888888888","hola@email.com"))