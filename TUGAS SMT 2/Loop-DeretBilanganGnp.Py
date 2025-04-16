# Input dari keyboard
n = 10

print("Bilangan genap dari 0 sampai", n, ":")
for i in range(0, n + 1):
    if i % 2 == 0:
        print(i, end=" ")