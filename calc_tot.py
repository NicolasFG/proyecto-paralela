import matplotlib.pyplot as plt

def show_tot():
    N = [4, 8, 16, 32, 64]
    P = [1, 2, 4, 8, 16, 32]
    times = [
        [4.66e1, 2.09e2, 9.67e2, 4.36e3, 2.00e4],
        [2.35e1, 1.05e2, 4.83e2, 2.18e3, 1.01e4],
        [1.18e1, 5.27e1, 2.42e2, 1.09e3, 5.01e3],
        [6.11e0, 2.68e1, 1.22e2, 5.48e2, 2.51e3],
        [3.23e0, 1.38e1, 6.21e1, 2.77e2, 1.26e3],
        [2.89e0, 9.73e0, 3.55e1, 1.49e2, 6.53e2]
    ]

    for i, p in enumerate(P):
        plt.subplot(2, 2, 4)
        plt.plot(N, times[i], label=f'P = {p}')

    plt.xlabel('Cantidad de N')
    plt.ylabel('Tiempo')
    plt.title('Tiempo(Segundos) vs Cantidad de Cuerpos (N)')
    plt.legend()
    #plt.show()
    