import math as m
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np
x = np.linspace(-3*m.pi ,3*m.pi, 250)
y =np.sin(x)
plt.figure(figsize=(10, 5))
plt.scatter(x,y,
 s=300,
 marker='s',
 c='violet',
 lw=2,
 edgecolor='black',
 hatch='**'
 )
plt.plot(x,y,lw = 4, color = 'red',zorder = 0)
plt.title(
 label='$sin(x)$ with random noise', # Заголовок
 fontsize=20 # Размер шрифта
)
plt.xlabel('x range', fontsize=18)
plt.ylabel('y range', fontsize=18)
plt.tick_params(labelsize=16)
plt.xticks(
 ticks=np.arange(-10, 11, 2) # Нужные значения по оси x
)
plt.yticks(ticks=np.arange(-1.5, 2,0.5))
plt.show()