import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class BorrarContacto:
    def GET(self, id_contacto):
        modelo = ModelContactos()
        resultado = modelo.buscarContacto(int(id_contacto))
        return render.borrar_contacto(resultado[0])