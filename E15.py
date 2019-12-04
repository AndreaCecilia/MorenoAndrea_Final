import numpy as np
import matplotlib.pyplot as plt

datos=np.loadtxt('valores.txt')
def probabilidad_sigma(sigma, xd, beta=3.0):
    probabilidad=(1/(sigma*np.sqrt(2*np.pi))*np.exp(-1/2*((xd**2)/sigma**2)))
    return(probabilidad)

def likelihood(sigma, x_data):
    l = 1.0
    for x in x_data:
        l = l * probabilidad_sigma(sigma, x)
    return l

def sigma_metropolis(x_data, N=10**5, delta=1.0):
    lista = [np.random.random()]

    for i in range(1,N):
        propuesta  = lista[i-1] + (np.random.random())*delta
        r = min(1, likelihood(propuesta, x_data)/likelihood(lista[i-1], x_data))
        gamma = np.random.random()
        if(gamma < r):
            lista.append(propuesta)
        else:
            lista.append(lista[i-1])
    return np.array(lista)


plt.figure()
plt.subplots_adjust(hspace=0.4)
plt.subplots_adjust(wspace=0.4)


sigma = sigma_metropolis(datos, N=10**5, delta=1.0)



_ = plt.hist(sigma, bins=40, density=True)

plt.xlabel(r'$\sigma$')
plt.ylabel(r'P($\sigma$|x_k)')
label = 'x = {}'.format(datos)
plt.title(('media=',np.mean(sigma),'desviación', np.std(sigma)))
plt.savefig("sigma.png", bbox_inches="tight")