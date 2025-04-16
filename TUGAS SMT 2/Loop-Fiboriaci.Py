def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
    return sequence[:n]

# Contoh penggunaan:
jumlah = int(input("Masukkan jumlah bilangan Fibonacci: "))
print(f"Deret Fibonacci sebanyak {jumlah} angka:")
print(fibonacci(jumlah))