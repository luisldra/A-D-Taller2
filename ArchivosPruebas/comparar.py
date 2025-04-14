import pandas as pd

def comparar_excels(archivo1, archivo2):
    xls1 = pd.read_excel(archivo1, sheet_name=None, engine='openpyxl')
    xls2 = pd.read_excel(archivo2, sheet_name=None, engine='openpyxl')

    diferencias = []

    hojas1 = set(xls1.keys())
    hojas2 = set(xls2.keys())
    if hojas1 != hojas2:
        diferencias.append(f"Hojas diferentes: {hojas1.symmetric_difference(hojas2)}")

    hojas_comunes = hojas1.intersection(hojas2)

    for hoja in hojas_comunes:
        df1 = xls1[hoja].fillna("").astype(str)
        df2 = xls2[hoja].fillna("").astype(str)

        if df1.shape != df2.shape:
            diferencias.append(f"Diferente tamaño en hoja '{hoja}': {df1.shape} vs {df2.shape}")
            continue

        for fila in range(df1.shape[0]):
            for col in range(df1.shape[1]):
                val1 = df1.iat[fila, col]
                val2 = df2.iat[fila, col]
                if val1 != val2:
                    diferencias.append(f"Diferencia en hoja '{hoja}' - Fila {fila+1}, Columna {col+1}: '{val1}' ≠ '{val2}'")

    if not diferencias:
        return "Los archivos son iguales."
    else:
        resultado = "Diferencias encontradas:\n"
        resultado += "\n".join(diferencias)
        return resultado

resultado = comparar_excels("PruebasQNodesN20.xlsx", "PruebasQNodesCambiosFinales_20.xlsx")
print(resultado)
