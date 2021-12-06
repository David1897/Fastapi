from peewee import *
from modelos import *

db = SqliteDatabase('tarea8.db')

class Factura(Model):
    fecha = TextField()
    cliente_id = IntegerField()
    description = TextField()
    subtotal = DoubleField()
    itbis = DoubleField()
    total = DoubleField()
    usuario = IntegerField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Factura_Detalle(Model):
    factura_id = ForeignKeyField(Factura, backref='detalle')
    codigo = TextField()
    nombre = TextField()
    precio = FloatField()
    cantidad = FloatField()
    total = FloatField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Clientes(Model):
    correo = TextField()
    nombre = TextField()
    apellido = TextField()
    rnc = TextField()
    telefono = TextField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Articulos(Model):
    codigo = TextField()
    Tipo = TextField()
    nombre = TextField()
    precio = FloatField()
    cantidad = IntegerField()
    comentario = TextField()

    class Meta:
        database = db # This model uses the "people.db" database.

db.connect()

db.create_tables([Factura, Factura_Detalle, Clientes, Articulos])

#crud de facturas

def guardarFactura(obj:facturas):
  fac = Factura()
  fac.cliente_id = obj.cliente_id
  fac.fecha = obj.fecha
  fac.description = obj.descripcion
  fac.subtotal = obj.subtotal
  fac.itbis = obj.itbis
  fac.total = obj.total
  fac.usuario = obj.usuario
  fac.save()

  for dett in obj.detalle:
    det = Factura_Detalle()
    det.factura_id = fac
    det.codigo = dett.codigo
    det.nombre = dett.nombre
    det.precio = dett.precio
    det.cantidad = dett.cantidad
    det.total = dett.total
    det.save()


def cargar_facturas():
  pokemoness = []
  for per in Factura.select().dicts():
    pokemoness.append(per)
  return pokemoness 

def actualizarFactura(obj:facturas):
  fac = Factura.get(Factura.id == obj.id)
  fac.cliente_id = obj.cliente_id
  fac.fecha = obj.fecha
  fac.description = obj.descripcion
  fac.subtotal = obj.subtotal
  fac.itbis = obj.itbis
  fac.total = obj.total
  fac.usuario = obj.usuario
  fac.save()

  for dett in obj.detalle:
    det = Factura_Detalle()
    det.factura_id = fac
    det.codigo = dett.codigo
    det.nombre = dett.nombre
    det.precio = dett.precio
    det.cantidad = dett.cantidad
    det.total = dett.total
    det.save()

def eliminarFacturas(obj:facturas):
    qry=Factura.delete().where (Factura.id == obj.id)
    qry.execute()

#crud clientes    

def guardarClientes(obj:cliente):
  per = Clientes()
  per.correo = obj.correo
  per.nombre = obj.nombre
  per.apellido = obj.apellido
  per.rnc = obj.rnc
  per.telefono = obj.telefono
  per.save()


def cargar_clientes():
  clientess = []
  for per in Clientes.select().dicts():
    clientess.append(per)
  return clientess 

def actualizarCliente(obj:cliente):
  per = Clientes.get(Clientes.id == obj.id)
  per.correo = obj.correo
  per.nombre = obj.nombre
  per.apellido = obj.apellido
  per.rnc = obj.rnc
  per.telefono = obj.telefono
  per.save()

def eliminarCliente(obj:cliente):
    qry=Clientes.delete().where (Clientes.id == obj.id)
    qry.execute()

#crud articulos    

def guardarArticulo(obj:articulo):
  per = Articulos()
  per.codigo = obj.codigo
  per.Tipo = obj.tipo
  per.nombre = obj.nombre
  per.precio = obj.precio
  per.cantidad = obj.cantidad
  per.comentario = obj.comentario
  per.save()


def cargar_articulos():
  articuloss = []
  for per in Articulos.select().dicts():
    articuloss.append(per)
  return articuloss 

def actualizarArticulos(obj:articulo):
  per = Articulos.get(Articulos.id == obj.id)
  per.codigo = obj.codigo
  per.Tipo = obj.tipo
  per.nombre = obj.nombre
  per.precio = obj.precio
  per.cantidad = obj.cantidad
  per.comentario = obj.comentario
  per.save()

def eliminarArticulos(obj:articulo):
    qry=Articulos.delete().where (Articulos.id == obj.id)
    qry.execute()    