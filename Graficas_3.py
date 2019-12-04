import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt('data.dat')
plt.figure(figsize=(14,4))
x = np.linspace(0,2,200)
delta_t = 1.0/100
i=int(0.5/0.01)
plt.scatter(x, data[0,:])
plt.plot(x, data[i,:])
    
plt.xlabel("Posicion")
plt.ylabel("$u$")
            
plt.savefig('resultado.png')