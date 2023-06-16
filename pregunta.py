"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df = df.dropna() 

    def organizarFechas(fecha):
        partes = fecha.split('/')
        p1, p2, p3 = partes[0], partes[1], partes[2]
        if len(p1) == 4:
            date = '/'.join(reversed(partes))
        else:
            date = '/'.join(partes)
        return date

    df['sexo'] = df.sexo.str.lower()
    df['tipo_de_emprendimiento'] = df.tipo_de_emprendimiento.str.lower()
    df['idea_negocio'] = df.idea_negocio.str.lower()
    df['idea_negocio'] = df.idea_negocio.str.replace('_', ' ')
    df['idea_negocio'] = df.idea_negocio.str.replace('-', ' ')
    df['idea_negocio'] = df.idea_negocio.str.strip()
    df['barrio'] = df.barrio.str.lower()
    df['barrio'] = df.barrio.str.replace('_', ' ')
    df['barrio'] = df.barrio.str.replace('-', ' ')
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(organizarFechas)
    df['monto_del_credito'] = df.monto_del_credito.str.replace(' ', '')
    df['monto_del_credito'] = df.monto_del_credito.str.replace('$', '')
    df['monto_del_credito'] = df.monto_del_credito.str.replace(',', '')
    df.monto_del_credito = df.monto_del_credito.astype(float)
    df['línea_credito'] = df.línea_credito.str.lower()
    df['línea_credito'] = df.línea_credito.str.replace('_', ' ')
    df['línea_credito'] = df.línea_credito.str.replace('-', ' ')
    df = df.drop_duplicates(
            subset=["sexo", "tipo_de_emprendimiento", 'idea_negocio', 'barrio', 'estrato', 'comuna_ciudadano', 
            'fecha_de_beneficio','monto_del_credito', 'línea_credito'],
        )
    return df
