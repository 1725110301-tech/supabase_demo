from supabase import create_client, Client
from dotenv import load_dotenv
import os

import logging

load_dotenv()
logger=logging.getLogger(__name__)


class AuthUsers:
    def __init__(self) -> None:
        try:
            self.supabase: Client = create_client(
                os.environ.get("SUPABASE_URL", ""),
                os.environ.get("SUPABASE_KEY", "")
            )
        except Exception as error:
            logger.error(f"Error 100: {str(error)}")
            print(f"ERROR 100: {error.args[0]}")
    def iniciarSesion(self,email:str,password:str):
        try:
            response = self.supabase.auth.sign_in_with_password({
                "email":email,
                "password":password
            })
            ##print(f"Inicio de sesión exitoso: {response.session}")
            return response.session.access_token
        except Exception as error:
            logger.error(f"Error 106: {str(error)}")
            print(f"ERROR 106: {error.args[0]}")
            return None
        
    def registrarUsuario(self,email:str,password:str)->str | None:
        try:
            response=self.supabase.auth.sign_up({
                "email":email,
                "password":password
            })
            print(f"Usuario registrado")
            return response.user.id
        except:
             logger.error(f"Error 107: {str(error)}")
             print(f"ERROR 107: {error.args[0]}")
             return None
if __name__=="__main__":
    print("Autenticacion de usuarios")
    objeto= AuthUsers()
    print(objeto.iniciarSesion("dejah@email.com","1234567"))
    print(objeto.registrarUsuario("john@email.com","1234567"))