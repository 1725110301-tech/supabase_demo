import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class BorrarContacto:
    def GET(self, id_contacto):
        modelo = ModelContactos()
        resultado = modelo.buscarContacto(int(id_contacto))
        return render.borrar_contacto(resultado[0])
    
    def POST(self,id_contacto):
        modelo = ModelContactos()
        modelo.borrarContacto(id_contacto)
        html = '''
        <h1>Contacto borrado correctamente</h1>
        <a href="/contactos">Regresar</a>
        '''

        return html