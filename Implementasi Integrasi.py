import numpy as np
import time

# Fungsi f(x) yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Metode integrasi Simpson 1/3
def simpson_integration(a, b, N):
    if N % 2 == 1:
        N += 1
    h = (b - a) / N
    integral = f(a) + f(b)
    for i in range(1, N, 2):
        integral += 4 * f(a + i * h)
    for i in range(2, N, 2):
        integral += 2 * f(a + i * h)
    integral *= h / 3
    return integral

# Menghitung galat RMS antara nilai pi yang diaproksimasi dan nilai referensi pi
def calculate_rms_error(approx_pi, true_pi):
    return np.sqrt(np.mean((approx_pi - true_pi) ** 2))

def main():
    true_pi = 3.14159265358979323846
    N_values = [10, 100, 1000, 10000]
    method_name = "Simpson 1/3 Integration"
    nim = "21120122140123"
    
    print(f'NIM: {nim}, Metode yang digunakan: {method_name}\n')
    results = []
    for N in N_values:
        start_time = time.time()
        approx_pi = simpson_integration (0, 1, N)
        end_time = time.time()
 rms_error = calculate_rms_error(approx_pi, true_pi)
        exec_time = end_time - start_time
        results.append((N, approx_pi, rms_error, exec_time))
    
    for result in results:
        print(f'N = {result[0]}, Approximated Pi = {result[1]}, RMS Error = {result[2]}, Execution Time = {result[3]} seconds')
    print("\n")

if __name__ == "__main__":
    main()
