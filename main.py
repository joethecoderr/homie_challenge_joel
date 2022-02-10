
from src.extract import leer_rentas_csv, leer_vecindarios_csv
from src.transform import ligar_coordenadas_a_vecindario, limpiar_rentas_df, limpiar_vecindarios_df
from src.load import load_to_sqllite
from src.statistics import obtener_estadistica


def run():
    option = int(input())
    if option == 1:
        rentas_df = leer_rentas_csv()
        vecindarios_df = leer_vecindarios_csv()
        rentas_df = limpiar_rentas_df(rentas_df)
        vecindarios_df = limpiar_vecindarios_df(vecindarios_df)
        rentas_vecindarios_df = ligar_coordenadas_a_vecindario(rentas_df, vecindarios_df)
        load_to_sqllite(rentas_vecindarios_df)
        print("Informacion procesada y cargada con exito!")
    elif option == 2:
        obtener_estadistica()
    else:
        print("Opcion Invalida")

if __name__ == '__main__':
    print("*" * 50)
    print("Homie numbers\n\nSelecciona una opcion \n\n1)Leer data y cargar a la BD \n2)Consultar estadisticas mas relevantes\n")
    print("*" * 50)
    run()