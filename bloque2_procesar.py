import pandas as pd
 
datos = {
    'reactor':     ['R1','R1','R1','R2','R2','R2','R3','R3'],
    'turno':       ['manana','tarde','noche','manana','tarde','noche','manana','tarde'],
    'temperatura': [85, 92, 78, 95, 88, 91, 76, 83],
    'eficiencia':  [91.2, 87.5, 94.1, 83.3, 89.7, 85.0, 96.4, 92.8],
    'incidentes':  [0, 1, 0, 2, 0, 1, 0, 0]
}
 
df = pd.DataFrame(datos)

#Ejercicio 2.1
#Ejemplo
print(df['temperatura'])
print(df[['reactor', 'eficiencia']])
print(df.head(4))

#Imprime solo la columna 'turno'
print(df['turno'])
#Imprime las columnas 'reactor' e 'incidentes' juntas
print(df[['reactor','incidentes']].head(4))

#Ejercicio 2.2
#Ejemplo
calientes=df[df['temperatura']>88]
print('Mediciones con temperatura mayor a 88: ')
print(calientes.to_string())

#Filtro 1 turno: mañana
manana=df[df['turno']=='manana']
print('Turno manana:')
print(manana.to_string())

#Filtro 2 sin incidentes
sin_incidentes=df[df['incidentes']==0]
print('Sin incidentes:')
print(sin_incidentes.to_string())

#Ejercicio 2.3
#Ejemplo
promedio_temp=df.groupby('reactor')['temperatura'].mean()
print(promedio_temp)

#Eficiencia promedio
ef_turno=df.groupby('turno')['eficiencia'].mean()
print('Eficiencia promedio por turno:')
print(ef_turno)

#Incidentes por reactor
inc_reactor=df.groupby('reactor')['incidentes'].sum()
print('Total incidentes por reactor:')
print(inc_reactor)

