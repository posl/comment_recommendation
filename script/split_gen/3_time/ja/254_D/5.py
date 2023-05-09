def main():
    n = int(input())
    c = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i * j <= n and (i * j) ** 0.5 % 1 == 0:
                c += 1
    print(c)
