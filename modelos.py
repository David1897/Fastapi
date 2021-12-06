from pydantic import BaseModel
from typing import List, Optional


class factura_detalle(BaseModel):
    factura_id:int
    codigo:str
    nombre:str
    precio:float
    cantidad:float
    total:float  

class facturas(BaseModel):
    id:int
    fecha:str
    cliente_id:int
    descripcion:str
    subtotal:float
    itbis:float
    total:float
    usuario:int
    detalle: List[factura_detalle] = []

class cliente(BaseModel):
    id:int
    correo:str
    nombre:str
    apellido:str
    rnc:str
    telefono:str

class articulo(BaseModel):
    id:int
    codigo:str
    tipo:str
    nombre:str
    precio:float
    cantidad:int
    comentario:str     