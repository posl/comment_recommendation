def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    b[0] = sum(a) - (n - 2) * a[1]
    b[0] //= 2
    for i in range(1, n):
        b[i] = a[i - 1] - b[i - 1]
    print(*b)
