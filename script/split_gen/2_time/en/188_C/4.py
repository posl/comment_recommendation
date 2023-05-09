def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (2 ** n)
    for i in range(n):
        for j in range(2 ** i):
            if a[2 * j] > a[2 * j + 1]:
                b[j] = a[2 * j]
                a[j] = a[2 * j]
            else:
                b[j] = a[2 * j + 1]
                a[j] = a[2 * j + 1]
    print(a.index(b[-1]) + 1)
