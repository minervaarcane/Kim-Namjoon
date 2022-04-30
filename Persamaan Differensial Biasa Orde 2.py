# FISIKA MATEMATIK 1
# RIANA OKTAFIANTI | 21030224040 | FISIKA 2021 E
# NO 10-B 

# Second Order Differential

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def f(y,x):
    return(y[1],5*y[1]-6*y[0])

#Actual solution
ya=lambda x: (-1)*np.exp(3*x)+ (2)*np.exp(2*x)

y0=[1,1]
xs=np.arange(0,0.8,0.2)
us=odeint(f,y0,xs)
ys=us[:,0]
print (us)
plt.plot(xs,ys,'ro',label="numeric solution")
plt.plot(xs,ya(xs),label="actual solution")
plt.xlabel('x values')
plt.ylabel('y values')
plt.legend(loc='lower right', prop={'size':10})
plt.show()
