import web
from mvc.controllers.model_contactos import ModelContactos

render= web.template.render('mvc/views', base='template')

class Contactos:
    def GET(self):
        model_contactos= ModelContactos() 
        print(model_contactos.obtenerContactos())
        return render.index()
