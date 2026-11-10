import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class VerContacto:
    def GET(self, id_contacto):
        model_contactos = ModelContactos()         
        resultado = model_contactos.buscarContacto(int(id_contacto))


        return render.ver_contacto(resultado[0])  