from sympy import symbols
from sympy.plotting import plot3d
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

print('**************************************')
print('Gráfico de Funções de Várias Variáveis')
print('**************************************')

x, y, z = symbols('x y z')

z = input('Função f(x,y) = ')

plot1 = plot3d(z, xlabel='\nEixo X', ylabel='\nEixo Y', title=z, show=False)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

backend = plot1.backend(plot1)
backend.ax = ax
backend._process_series(backend.parent._series, ax, backend.parent)
plt.close(backend.fig)
ax.collections[0].set_cmap('viridis')
plt.colorbar(ax.collections[0])
plt.show()
