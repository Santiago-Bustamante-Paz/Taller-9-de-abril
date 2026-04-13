import pandas as pd
 
datos = {
    'reactor':     ['R1','R1','R1','R2','R2','R2','R3','R3'],
    'turno':       ['manana','tarde','noche','manana','tarde','noche','manana','tarde'],
    'temperatura': [85, 92, 78, 95, 88, 91, 76, 83],
    'eficiencia':  [91.2, 87.5, 94.1, 83.3, 89.7, 85.0, 96.4, 92.8],
    'incidentes':  [0, 1, 0, 2, 0, 1, 0, 0]
}
 
df = pd.DataFrame(datos)
print(df)
 
print('--- Filas y columnas ---')
print(df.shape)
 
print('--- Tipo de dato de cada columna ---')
print(df.dtypes)
 
print('--- Estadísticas básicas ---')
print(df.describe().round(2))