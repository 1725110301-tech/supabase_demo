import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class Contactos:
<<<<<<< Updated upstream
    def GET(self):
        model_contactos = ModelContactos()
        lista = model_contactos.obtenerContactos()
        print(lista)
        return render.contactos(lista)
=======
    try:
        def GET(self):
            model_contactos = ModelContactos()
            lista = model_contactos.obtenerContactos()
            return render.contactos(lista)
        except Exception as error:
        print(f"ERROR 106: {error.args}")



>>>>>>> Stashed changes
