#Ejercicio 3.1
import pandas as pd
import matplotlib.pyplot as plt

datos = {
    'reactor':     ['R1','R1','R1','R2','R2','R2','R3','R3'],
    'turno':       ['manana','tarde','noche','manana','tarde','noche','manana','tarde'],
    'temperatura': [85, 92, 78, 95, 88, 91, 76, 83],
    'eficiencia':  [91.2, 87.5, 94.1, 83.3, 89.7, 85.0, 96.4, 92.8],
    'incidentes':  [0, 1, 0, 2, 0, 1, 0, 0]
}
 
df = pd.DataFrame(datos)

promedio_temp=df.groupby('reactor')['temperatura'].mean()

plt.figure(figsize=(7,4))

plt.bar(promedio_temp.index,promedio_temp.values,color='steelblue')

plt.title('Temperatura promedio por reactor')
plt.xlabel('Reactor')
plt.ylabel('Temperatura (C)')
plt.tight_layout()
plt.show()

#Ejemplo 3.2
plt.figure(figsize=(7,4))
plt.scatter(df['temperatura'],df['eficiencia'],color='coral',s=80)
plt.title('Temperatura vs Eficiencia')
plt.xlabel('Temperatura (C)')
plt.ylabel('Eficiencia (%)')
plt.tight_layout()
plt.show()

#Ejercicio 3.3
plt.figure(figsize=(8,4))
plt.plot(df.index,df['eficiencia'],marker='o',linewidth=2,color='green')
plt.title('Eficiencia por medicion')
plt.xlabel('Numero de medicion')
plt.ylabel('Eficiencia (%)')
plt.tight_layout()
plt.show()
