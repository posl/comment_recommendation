def main():
    n = int(input())
    # n = 100000
    # n = 8
    a = []
    for i in range(2, int(n ** 0.5) + 1):
        x = i * i
        while x <= n:
            a.append(x)
            x *= i
    print(n - len(set(a)))
