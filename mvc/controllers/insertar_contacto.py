import web
from mvc.models.model_contactos import ModelContactos

render = web.template.render('mvc/views', base='template')


    #insertar contacto html
class InsertarContacto: 
    def GET(self):
        return render.insertar_contacto()
        pass
    
    #Recibe los input del formulario y accede a cada uno
    #utilizando el atributo 'name'
    def POST(self):
        formulario = web.input()
        nombre = formulario['nombre']
        email = formulario['email']
        telefono = formulario['telefono']
        
        print(f"Nombre: {nombre}")
        print(f"Email: {email}")
        print(f"Teléfono: {telefono}")
        
        modelo= ModelContactos()
        modelo.insertarContacto(nombre,telefono,email)
        html= '''
        <h1>Contacto almacenado correctamente</h1>
        <a href="/contactos">Regresar</a>
        '''
        
        return html
        
        