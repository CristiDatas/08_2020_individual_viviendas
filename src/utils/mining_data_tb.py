# Module dedicated to data wrangling functions
import pandas as pd

# Función hacer_df() de mining_tb que recibe como parámetro un archivo de excel, hace un dataframe con sólo la primera hoja y sólo las 2 primeras columnas poniendo como índice la primera y, luego, mediante un for va recorriendo el resto de las hojas concatenando la segunda columna de cada una al primer dataframe. La función devuelve un dataframe con las fechas como índice y los precios de cada ámbito geográfico como columnas.

def hacer_df(archivo):

    nombre_df=pd.read_excel(archivo,sheet_name=0,index_col=0,usecols=[0,1])

    for sheet in range(1,26):
        nombre_df=pd.concat((nombre_df,pd.read_excel(archivo,sheet_name=sheet,index_col=0,usecols=[0,1])),axis=1)
    
    return nombre_df

# Función hacer_float() de mining_tb que toma como parámetro un dataframe, hace una copia, elimina los caracteres no numéricos, el 2 de m² y si hay alguna coma (para decimales) la cambia por un punto.  para después convertir las cadenas numéricas a float. La función devuelve un dataframe con valores tipo float.
def hacer_float(dataframe):
    nombre=dataframe.copy()
    nombre.replace(regex=True, inplace=True, to_replace=r"\.|\D{2}|2$", value=r"")
    nombre.replace(regex=True, inplace=True, to_replace=r"\,", value=r".")
    for c in nombre.columns:
        nombre[c]=pd.to_numeric(nombre[c],downcast="float")
    return nombre

# Función seleccion_columnas() de mining_tb para seleccionar el ámbito (columnas) a analizar. La función toma como parámetros un dataframe y la posicion de dos columnas para seleccionar un rango. La función devuelve la lista de esas columnas selecionadas.

def seleccion_columnas(dataframe,col1,col2):
    columnas=dataframe.columns[col1:col2]
    return columnas

