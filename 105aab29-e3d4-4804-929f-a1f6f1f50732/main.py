def calculate_sum(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

print(calculate_sum(10))