import pysd
import matplotlib.pyplot as plt

modelo = pysd.read_vensim('untitled.mdl')
valores = modelo.run(return_columns=['almacen'])
tabla = valores.head(10)
print(tabla)
valores.plot()

