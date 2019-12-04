import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('data.dat')
plt.figure(figsize=(14,4))
x = np.linspace(0,2,200)
delta_t = 1.0/100
i=0.5
if i%(100//9) == 0:
    plt.plot(x, data[i,:], alpha=(i+1)/100, color='black', label="t={:.02f}".format(i*0.01))
    plt.legend(loc=1)
    plt.xlabel("Posicion")
    plt.ylabel("$\psi$")
            

plt.savefig('resultado.png')