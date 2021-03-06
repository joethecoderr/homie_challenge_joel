
from db import engine

def obtener_estadistica():
    rentas_mas_altas = obtener_colonia_renta_mas_alta()
    mas_casas_renta = obtener_colonias_mas_rentas()
    habitaciones_promedio_vecindario, vecindario = obtener_habitaciones_promedio_vecindario()
    porcentaje_estacionamiento = obtener_porcentaje_estacionamiento_vecindario()
    print(f"La colonia con la renta promedio mas elevada es: { rentas_mas_altas[0][1] } , con una renta promedio de: ${ rentas_mas_altas[0][0] } \n\n\n")
    print("Las 10 colonias con mas inmuebles en renta son: \n")
    for element in mas_casas_renta:
        print(f"- {element[1]}: {element[0]} en renta")
    print('')
    print(f"El promedio de habitaciones en {vecindario} es de {habitaciones_promedio_vecindario[0][0]: .2f} \n\n")
    print("El promedio de inmuebles que cuentan con estacionamiento por cada vecindacio es de: ")
    for element in porcentaje_estacionamiento:
        print(f"- {element[1]}: {element[0]:.2f}% de inmuebles que cuentan con estacionamiento ")

def obtener_colonia_renta_mas_alta():
    query = "SELECT AVG(PRECIO) as promedio, nombre FROM 'RentasVecindarios' group by nombre order by promedio desc limit 1"
    conn = engine.connect()
    resultado = conn.execute(query).fetchall()
    return resultado

def obtener_colonias_mas_rentas():
    query = "SELECT COUNT(*) as total_rentas, nombre from RentasVecindarios  group by nombre order by total_rentas desc limit 10"
    conn = engine.connect()
    resultado = conn.execute(query).fetchall()
    return resultado

def obtener_habitaciones_promedio_vecindario(vecindario='JACARANDAS'):
    query = f"SELECT AVG(habitaciones) as habitaciones_promedio FROM 'RentasVecindarios' group by nombre  having nombre = '{vecindario}'"
    conn = engine.connect()
    resultado = conn.execute(query).fetchall()
    return resultado, vecindario

def obtener_porcentaje_estacionamiento_vecindario():
    query = "SELECT  CAST(COUNT(IIF(estacionamiento=1, 1, null)) AS FLOAT) / COUNT(estacionamiento)*100 as porcentaje_estacionamiento, nombre FROM 'RentasVecindarios' group by nombre limit 20"
    conn = engine.connect()
    resultado = conn.execute(query).fetchall()
    return resultado