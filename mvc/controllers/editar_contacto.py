import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class EditarContacto:
    def GET(self, hash_contacto):
        modelo = ModelContactos()
        resultado = modelo.buscarContacto(hash_contacto)
        if not resultado:
            return "<h1>Contacto no encontrado</h1><a href='/contactos'>Regresar</a>"
        return render.editar_contacto(resultado[0])

    def POST(self, hash_contacto):
        formulario = web.input()
        modelo = ModelContactos()
        modelo.actualizarContacto(
            hash_contacto,
            formulario['nombre'],
            formulario['telefono'],
            formulario['email']
        )
        return '''
    <h1>Contacto actualizado correctamente</h1>
    <a href="/contactos">Regresar</a>
    '''