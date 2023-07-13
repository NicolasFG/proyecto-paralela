import os
import calc_comm
import calc_tot
import calc_speedup
import calc_efficiency
import matplotlib.pyplot as plt

# procesadores y N
n_processors = [2, 4, 8, 16, 32, 64]
n_values = [4, 8, 16, 32, 64]

# tiempo secuencial
seq_times = [4.66E+01, 2.09E+02, 9.67E+02, 4.36E+03, 2.00E+04]

for p in n_processors:
    for i in enumerate(n_values):
        file_name = f"p{p}_{i[1]}.txt"
        file_path = os.path.join("out/", file_name)
        if os.path.isfile(file_path):
            # metricas
            t_gflops = 0.0
            t_comm = 0.0
            t_force = 0.0
            t_tot = 0.0

            with open(file_path, "r") as file:
                lines = file.readlines()

            for line in lines:
                if "Real Speed" in line:
                    t_gflops = float(line.split("=")[1].strip().split(" ")[0])
                elif "comm :" in line:
                    t_comm = float(line.split(":")[1].split()[0])
                elif "force:" in line:
                    t_force = float(line.split(":")[1].split()[0])
                elif "tot  :" in line:
                    t_tot = float(line.split(":")[1].split()[0])

            # speedup y efficiency
            speedup = seq_times[i[0]] / t_tot
            efficiency = speedup / p

            print(f"P: {p}")
            print(f"N: {i[1]}")
            print(f"Tiempo en GFlops: {t_gflops}")
            print(f"T comm: {t_comm}")
            print(f"T force: {t_force}")
            print(f"T tot: {t_tot}")
            print(f"Speedup: {speedup}")
            print(f"Efficiency: {efficiency}")
            print()

plt.figure(figsize=(10, 8))
plt.title("Análisis de performance")

calc_comm.show_comm()
calc_tot.show_tot()
calc_speedup.show_speedup()
calc_efficiency.show_efficiency()

plt.tight_layout()

plt.show()