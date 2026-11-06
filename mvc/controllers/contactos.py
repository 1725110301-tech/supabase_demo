import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class Contactos:
    def GET(self):
        model_contactos = ModelContactos()
        lista = model_contactos.obtenerContactos()
        print(lista)
        return render.contactos(lista)