import geopandas as gpd
def transformar_letras_a_numero(rentas_df):
    text_to_number_dict = {
        "uno" : 1.0,
        "one" : 1.0,
        "uno y medio" : 1.5,
        "dos" : 2,
        "tres" : 3,
        "cuatro" : 4,
        "cinco" : 5,
        "seis" : 6,
        "siete" : 7
    }
    rentas_df.replace({"rooms": text_to_number_dict}, inplace=True)
    return rentas_df

def excluir_outliers(rentas_df):
    Q1 = rentas_df['precio'].quantile(0.25)
    Q3 = rentas_df['precio'].quantile(0.75)
    internal_range = Q3 - Q1
    rentas_df = rentas_df[~((rentas_df['precio'] < (Q1 - 1.5 * internal_range)) | (rentas_df['precio'] > (Q3 + 1.5 * internal_range)))]
    return rentas_df

def cambiar_nombres_columnas(rentas_df):
    nombres_espanol = {
        'Unnamed: 0':'id',
        'rooms': 'habitaciones',
        'bathrooms' : 'baños',
        'latitude': 'latitud',
        'longitude': 'longitud',
        'parking': 'estacionamiento',
        'date_in': 'fecha_registro'
    }
    rentas_df.rename(columns = nombres_espanol, inplace = True)
    return rentas_df

def limpiar_rentas_df(rentas_df):
    rentas_df = rentas_df[rentas_df['rooms'].notna()]
    rentas_df = transformar_letras_a_numero(rentas_df)
    rentas_df['rooms'].value_counts(dropna=False)
    rentas_df['bathrooms'].fillna(int( rentas_df['bathrooms'].median()),inplace=True )
    rentas_df['rooms'] = rentas_df['rooms'].astype(float)
    rentas_df['rooms'] = rentas_df['rooms'].astype(int)
    rentas_df = excluir_outliers(rentas_df)
    rentas_df = rentas_df[rentas_df['precio']>=1000]
    rentas_df = cambiar_nombres_columnas(rentas_df)
    rentas_df = transformar_longitud_a_negativa(rentas_df)

    return rentas_df


def limpiar_vecindarios_df(vecindarios_df): 
    vecindarios_df.drop(columns="id", inplace=True)
    nuevo_nombre = {
        'Unnamed: 0':'id',
    }
    vecindarios_df.rename(columns = nuevo_nombre, inplace = True)
    
    return vecindarios_df

def transformar_longitud_a_negativa(rentas_df):
    rentas_df['longitud'] = rentas_df['longitud'] * -1
    return rentas_df

def ligar_coordenadas_a_vecindario(rentas_df, vecindarios_df):
    rentas_geo_df = gpd.GeoDataFrame(rentas_df, geometry=gpd.points_from_xy(rentas_df.longitud, rentas_df.latitud))
    vecindarios_geo_df = gpd.GeoDataFrame(vecindarios_df, geometry = gpd.GeoSeries.from_wkb(vecindarios_df.geom))
    rentas_vecindarios = gpd.sjoin(rentas_geo_df, vecindarios_geo_df, op="within")
    rentas_vecindarios.reset_index(drop=True, inplace=True)
    rentas_vecindarios.drop(['id_left','id_right','index_right','geom', 'geometry', 'latitud', 'longitud'], axis=1, inplace=True)
    return rentas_vecindarios

