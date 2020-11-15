# Módulo dedicado a las funciones de gráficos (y también guardado como imágenes estáticas (.png) y dinámicas (.html)

import pandas as pd
import plotly
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Función evolucion() de visualization_tb para ver la evolución a lo largo de los años o meses del precio por m² de la vivienda en distintos ámbitos geográficos. La función toma como parámetros el dataframe a analizar, la operación que se quiera analizar ("venta" o "alquiler") y dos listas: una con los rangos de columnas o ámbitos geográficos a analizar y otra con los años de inicio del análisis hasta la actualidad. En los gráficos aparece sombreado el período del estado de alarma (desde el 14 de marzo al 21 de junio de 2020). Primero muestra la imagen de cada gráfico en modo interactivo y después guarda cada gráfico con su propio nombre descriptivo en la carpeta correspondiente a la operación dentro de plots en resources.

def evolucion(dataframe,ambito,years,operacion):

    for year in years:
        
        for a in ambito:
            name=a[0]+year
            im=plotly.plot(dataframe[:year][a],kind="line", title="EVOLUCIÓN DEL PRECIO DE "+operacion.upper()+" EN "+a[0]+" DESDE "+year,labels={"value":"euros/m²","Mes":"","variable":"Ámbito geográfico"},width=1000, height=650)
            im.add_shape(dict(type="rect",x0="2020-03-14",y0=0,x1="2020-06-21",y1=1,yref="paper", line=dict(            color="white",width=1),fillcolor="LightSkyBlue",opacity=0.4))
            im.show()

        for a in ambito:
            name=a[0]+year
            im=plotly.plot(dataframe[:year][a],kind="line",title="EVOLUCIÓN DEL PRECIO DE "+operacion.upper()+" EN "+a[0]+" DESDE "+year,labels={"value":"euros/m²","Mes":"","variable":"Ámbito geográfico"},width=1000, height=650)
            im.add_shape(dict(type="rect",x0="2020-03-14",y0=0,x1="2020-06-21",y1=1,yref="paper", line=dict(            color="white",width=1),fillcolor="LightSkyBlue",opacity=0.4))
            im.write_image("../resources/plots/"+operacion.lower()+"/"+operacion.lower()+name+".png")
            im.write_html("../resources/plots/"+operacion.lower()+"/"+operacion.lower()+name+".html")

# Función histo07() de visualization_tb para ver la frecuencia de precios desde 2007 en España, Barcelona provincia, Barcelona ciudad, Madrid provincia y Madrid ciudad. La función toma como parámetros el datafrme, el tipo de operacion (venta o alquiler) y la lista de columnas (ambito geográfico).

def histo07(dataframe, operacion, ambito):
    for a in ambito:
        px.histogram(dataframe, x=a,nbins=5,title="Precios "+operacion.lower()+" desde 2007 en "+operacion,width=400, height=300).show()
        px.histogram(dataframe, x=a,nbins=5,title="Precios "+operacion.lower()+" desde 2007 en "+operacion,width=400, height=300).write_image("../resources/plots/"+operacion.lower()+"/histo_"+operacion.lower()+a+"2007.png")
        px.histogram(dataframe, x=a,nbins=5,title="Precios "+operacion.lower()+" desde 2007 en "+operacion,width=400, height=300).write_html("../resources/plots/"+operacion.lower()+"/histo_"+operacion.lower()+a+"2007.html")

# Función reciente() de visualization_tb que compara el útimo valor del precio de la vivienda (julio de 2020) con el mínimo y máximo históricos desde 2007 o desde que se tengan datos. La función toma como parámetros el dataframe a analizar, la lista de listas de las columnas a comparar (ámbito geográfico) y el tipo de operación ("alquiler" o "venta").

def reciente(dataframe,ambito,operacion):
    for a in ambito:
        est=pd.concat((dataframe.describe()[1:],dataframe["2020-07-01"].copy()),axis=0)[a].T
        esp_est=est.iloc[:,[2,-1,6]]
        plotly.plot(esp_est,kind="bar",barmode="group",title="COMPARACIÓN RECIENTE CON EL MÍNIMO Y MÁXIMO HISTÓRICOS DE LA SERIE: "+operacion.upper()+" EN "+a[0],labels={"value":"euros/m²","index":"Ámbito geográfico","variable":"Valores"},width=1000, height=650).show()
        im=plotly.plot(esp_est,kind="bar",barmode="group",title="COMPARACIÓN RECIENTE CON EL MÍNIMO Y MÁXIMO HISTÓRICOS DE LA SERIE: "+operacion.upper()+" EN "+a[0],labels={"value":"euros/m²","index":"Ámbito geográfico","variable":"Valores"},width=1000, height=650)
        im.write_image("../resources/plots/"+operacion.lower()+"/minmax_"+operacion.lower()+a[0]+".png")
        im.write_html("../resources/plots/"+operacion.lower()+"/minmax_"+operacion.lower()+a[0]+".html")

# Función act_pie() de visualization_tb para ver el estado reciente de los precios en distintos ámbitos geográficos. La función toma como parámetros el dataframe de precios recientes, el ámbito geográfico (AUTONOMÍA O CIUDADES) y la operación (venta o alquiler) y devuelve un gráfico pie interactivo con la distribución de los valores correspondientes, primero lo mustra por pantalla y luego lo guarda en la carpeta correspondiente a su operación.

def act_pie(dataframe,ambito,operacion):
    px.pie(dataframe, values="JUL_20", names=ambito,title="Precios de "+operacion+" en julio de 2020 por "+ambito,width=1000, height=650).update_traces(textposition="inside", textinfo="label+value").show()
    px.pie(dataframe, values="JUL_20", names=ambito,title="Precios de "+operacion+" en julio de 2020 por "+ambito,width=1000, height=650).update_traces(textposition="inside", textinfo="label+value").write_image("../resources/plots/"+operacion.lower()+"/pie_"+operacion.lower()+ambito+"2020.png")
    px.pie(dataframe, values="JUL_20", names=ambito,title="Precios de "+operacion+" en julio de 2020 por "+ambito,width=1000, height=650).update_traces(textposition="inside", textinfo="label+value").write_html("../resources/plots/"+operacion.lower()+"/pie_"+operacion.lower()+ambito+"2020.html")

# Función hist_v_2020() de visualization_tb para ver la distribución de los precios según distintos ámbitos geográficos. La función toma como parámetro en dataframe, la operación (venta o alquiler) y el ámbito (AUTONOMÍA o CIUDADES) y devuelve un histograma interactivo de 5 bins que guarda en la carpera correspondiente a la operación.

def hist_v_2020(dataframe, ambito, operacion):
    px.histogram(dataframe, x="JUL_20",nbins=5,title="Distribución en julio de 2020 de los precios de "+operacion+" por "+ambito,width=1000, height=650).show()
    px.histogram(dataframe, x="JUL_20",nbins=5,title="Distribución en julio de 2020 de los precios de "+operacion+" por "+ambito,width=1000, height=650).write_image("../resources/plots/"+operacion.lower()+"/hist20_"+operacion.lower()+ambito+".png")
    px.histogram(dataframe, x="JUL_20",nbins=5,title="Distribución en julio de 2020 de los precios de "+operacion+" por "+ambito,width=1000, height=650).write_html("../resources/plots/"+operacion.lower()+"/hist20_"+operacion.lower()+ambito+".html")

# Función study_pie(), de visualization_tb que presenta un gráfico circular con la distribución de los 7 días de los que he dispuesto (por circunstancias personales) para hacer este estudio. El gráfico presenta el valor y el porcentaje y la función primero muestra el gráfico interactivo en pantalla y luego lo guarda en la carpeta resources tanto en .png como en .html.

def study_pie():
    px.pie(values=[2,1,1,2,1], names=["OBTENER DATOS","WRANGLING","MINERÍA/LIMPIEZA","VISUALIZACIÓN","INFORME"],title="Reparto del tiempo aproximado para este estudio (en días)",width=1000, height=650).update_traces(textposition="inside", textinfo="label+value+percent").show()
    px.pie(values=[2,1,1,2,1], names=["OBTENER DATOS","WRANGLING","MINERÍA/LIMPIEZA","VISUALIZACIÓN","INFORME"],title="Reparto del tiempo aproximado para este estudio (en días)",width=1000, height=650).update_traces(textposition="inside", textinfo="label+value+percent").write_image("../resources/pie_study_time.png")
    px.pie(values=[2,1,1,2,1], names=["OBTENER DATOS","WRANGLING","MINERÍA/LIMPIEZA","VISUALIZACIÓN","INFORME"],title="Reparto del tiempo aproximado para este estudio (en días)",width=1000, height=650).update_traces(textposition="inside", textinfo="label+value+percent").write_html("../resources/pie_study_time.html")

# Función corr_esp() de visualization_tb que recibe como un dataframe y las columnas referentes a España, Barcelona Y Madrid y devuelve la matriz de correlación de sus diferentes columnas. En este caso, sólo sirve para ver cómo es de parecida o diferente la evolución de los precios en Barcelona, Madrid y España.

def corr_esp(dataframe,col):
    matriz=dataframe[col]
    plt.figure(figsize=(10,7),tight_layout=True)
    c=matriz.corr()
    sns.heatmap(c,cmap="BrBG",annot=True)

# Función corr_mad() de visualization_tb que recibe como un dataframe y las columnas referentes a los distritos de Madrid  y devuelve la matriz de correlación de sus diferentes columnas. En este caso, sólo sirve para ver qué distritos de Madrid tienen una evolución de precios más parecida o más diferente.

def corr_mad(dataframe,col):
    matriz=dataframe[col]
    plt.figure(figsize=(20,15),tight_layout=True)
    c=matriz.corr()
    matriz=sns.heatmap(c,cmap="BrBG",annot=True)