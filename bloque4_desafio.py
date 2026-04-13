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

df['estado']=df['temperatura'].apply(lambda t:'crítico' if t>90 else 'normal')

print(df['estado'].value_counts().rename('estado'))

ef_reactor=df.groupby('reactor')['eficiencia'].mean()

colores=['green','blue','orange']

plt.figure(figsize=(7,4))
plt.bar(ef_reactor.index, ef_reactor.values, color=colores)
plt.title('Eficiencia promedio por reactor')
plt.xlabel('Reactor')
plt.ylabel('Eficiencia (%)')
plt.tight_layout()
plt.show()