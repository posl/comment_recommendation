def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (n + 1)
    for i in range(n, 0, -1):
        j = i * 2
        t = 0
        while j <= n:
            t += b[j]
            j += i
        if a[i - 1] != t % 2:
            b[i] = 1
    print(sum(b))
    for i in range(1, n + 1):
        if b[i] == 1:
            print(i, end=' ')
    print()
