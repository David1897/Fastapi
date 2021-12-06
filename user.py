from fastapi import APIRouter
from modelos import *
from typing import Optional
import database

user = APIRouter()


@user.get("/")
def inicio():
    return "Inicio del FastApi"

@user.post("/facturas/agregar",tags=['Facturas'])
def agregar_factura(fact:facturas):
  database.guardarFactura(fact)
  return {"msg": "Datos agregado"}


@user.put("/facturas/actualizar", tags=['Facturas'])
def actualizar_factura(per:facturas):
    database.actualizarFactura(per)
    return {"msg": "Datos actualizado"}   


@user.get("/facturas/lista", tags=['Facturas'])
def listarFacturas():
    tmp = database.cargar_facturas()
    return tmp


@user.delete("/facturas/eliminar", tags=['Facturas'])
def eliminar_factura(per:facturas):
    database.eliminarFacturas(per)
    return {"msg": "Datos eliminados"}

#crud de clientes en el FastApi

@user.post("/cliente/agregar",tags=['Clientes'])
def agregar_cliente(per:cliente):
  database.guardarClientes(per)
  return {"msg": "Datos agregado"}


@user.put("/cliente/actualizar", tags=['Clientes'])
def actualizar_cliente(per:cliente):
    database.actualizarCliente(per)
    return {"msg": "Datos actualizado"}   


@user.get("/cliente/lista", tags=['Clientes'])
def listarCliente():
    tmp = database.cargar_clientes()
    return tmp


@user.delete("/cliente/eliminar", tags=['Clientes'])
def eliminar_cliente(per:cliente):
    database.eliminarCliente(per)
    return {"msg": "Datos eliminados"}

#crud de Articulos en el FastApi

@user.post("/articulos/agregar",tags=['Articulos'])
def agregar_articulos(per:articulo):
  database.guardarArticulo(per)
  return {"msg": "Datos agregado"}


@user.put("/articulo/actualizar", tags=['Articulos'])
def actualizar_articulo(per:articulo):
    database.actualizarArticulos(per)
    return {"msg": "Datos actualizado"}   


@user.get("/articulos/lista", tags=['Articulos'])
def listarArticulos():
    tmp = database.cargar_articulos()
    return tmp


@user.delete("/articulo/eliminar", tags=['Articulos'])
def eliminar_articulo(per:articulo):
    database.eliminarArticulos(per)
    return {"msg": "Datos eliminados"}