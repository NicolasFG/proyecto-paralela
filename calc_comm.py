import matplotlib.pyplot as plt

def show_comm():
    N = [4, 8, 16, 32, 64]
    P = [1, 2, 4, 8, 16, 32]
    times = [
        [4.68e-3, 1.37e-2, 3.71e-2, 1.01e-1, 2.63e-1],
        [1.49e-1, 3.00e-1, 4.91e-1, 6.99e0, 8.30e0],
        [1.05e-1, 2.58e-1, 1.56e0, 1.30e0, 1.86e1],
        [1.78e-1, 3.64e-1, 1.38e0, 3.30e0, 1.27e1],
        [2.22e-1, 4.12e-1, 8.93e-1, 2.71e0, 1.28e1],
        [6.64e-1, 2.08e0, 2.47e0, 8.49e0, 1.29e1]
    ]
    
    for i, p in enumerate(P):
        plt.subplot(2, 2, 1)
        plt.plot(N, times[i], label=f'P = {p}')
    
    plt.xlabel('Cantidad de N')
    plt.ylabel('Tiempo')
    plt.title('Tiempo(Segundos) vs Cantidad de Cuerpos (N)')
    plt.legend()
    #plt.show()
