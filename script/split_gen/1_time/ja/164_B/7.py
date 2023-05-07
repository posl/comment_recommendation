def attack(a, b):
    return (a + b - 1) // b
a, b, c, d = map(int, input().split())
print('Yes' if attack(c, b) <= attack(a, d) else 'No')
