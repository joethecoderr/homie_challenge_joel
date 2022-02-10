#from models import RentasVecindarios
from db import engine
import pandas as pd
def load_to_sqllite(rentas_vecindarios_df):
    rentas_vecindarios_df.to_sql('RentasVecindarios', con=engine, index=True, index_label='id', if_exists='replace')
