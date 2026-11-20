import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class BorrarContacto:
    def GET(self, hash_contacto):
        modelo = ModelContactos()
        resultado = modelo.buscarContacto(hash_contacto)
        if not resultado:
            return "<h1>Contacto no encontrado</h1><a href='/contactos'>Regresar</a>"
        return render.borrar_contacto(resultado[0])

    def POST(self, hash_contacto):
        modelo = ModelContactos()
        modelo.borrarContacto(hash_contacto)
        return '''
        <h1>Contacto borrado correctamente</h1>
        <a href="/contactos">Regresar</a>
        '''