import pandas as pd
def leer_rentas_csv():
    rentas_df = pd.read_csv("./data/rents.csv", sep = ",")
    return rentas_df

def leer_vecindarios_csv():
    vecindarios_df = pd.read_csv("./data/neighbourhoods.csv", sep = ",")
    return vecindarios_df