# FISIKA MATEMATIK 1 | ICT 3
# RIANA OKTAFIANTI | 21030224040 | Fisika 2021 E
# No 10-A | Persamaan Differensial Biasa Orde 1

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint 

def f(y,x):
    return (y[1],x-x*y[0])

# Actual solution
ya=lambda x:1+(0)*np.exp((-1/2)*x**2)

y0=[1,0]
xs=np.arange(0,0.12,0.02)
us=odeint(f,y0,xs)
ys=us[:,0]
print(us)
plt.plot(xs,ys,'_')
plt.plot(xs,ys,'ro', label='numeric solution')
plt.plot(xs,ya(xs),label='actual solution')
plt.xlabel('x values')
plt.ylabel('y values')
plt.legend(loc='lower right',prop={'size':10})
plt.title('PDB Orde 1')
plt.show()
