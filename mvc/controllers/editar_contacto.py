import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')

class EditarContacto:
    def GET(self, id_contacto):
        modelo = ModelContactos()
        resultado = modelo.buscarContacto(int(id_contacto))
        return render.editar_contacto(resultado[0])

    def POST(self, id_contacto):
        formulario = web.input()
        modelo = ModelContactos()
        modelo.actualizarContacto(
            int(id_contacto),
            formulario['nombre'],
            formulario['telefono'],
            formulario['email']
        )
        return '''
    <h1>Contacto actualizado correctamente</h1>
    <a href="/contactos">Regresar</a>
    '''