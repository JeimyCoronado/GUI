import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/UNI/Taller de Dinámica de Sistemas/Datos/MOCK_DATA.csv')

print(df.to_string())

import matplotlib.pyplot as plt
x=[0,1,2,3,4,5,6,7,8,9,10]
y=[100,190,180,170,160,155,150,140,160,165,155]
plt.plot(x,y)
plt.show()