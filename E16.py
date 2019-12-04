import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt('monthrg.dat')
anio=data[:,0]
mes=data[:,1]
numdias=data[:,2] #si es 0 no hubo mediciones
mean_manchas=data[:,4] # -99 quiere decir que no hubo medición

listani=list(anio)
pos=listani.index(1900)
x=mean_manchas[pos:len(mean_manchas)]
def FT(x):
    N = len(x)
    X = np.zeros(N, dtype=complex)

    for k in range(N):
        X[k] = 0.0j
        for n in range(N):
            X[k] += x[n] * np.exp(-2.0 * np.pi * 1.0j / N ) ** (k * n) 
        
    return X

X = FT(x)
N = len(X)

plt.figure(figsize=(8,4.0))

plt.scatter(np.arange(N), np.abs(X/N))
plt.stem(np.arange(N), np.abs(X/N))
plt.xlabel('k')
plt.ylabel('|$X_k$|/N')
plt.title("Fourier")
plt.grid()

plt.figure(figsize=(20,10))
plt.plot(np.arange(len(mean_manchas[pos:len(mean_manchas)])),mean_manchas[pos:len(mean_manchas)])
plt.xlabel('tiempo en meses comenzando en el mes 0 el cual es Enero de 1900')
plt.ylabel('manchas promedio')
plt.title(2*np.pi/np.max(X))
plt.savefig('solar.png')