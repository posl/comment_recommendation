def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        if i % 2 == 0:
            b[0] += a[i]
        else:
            b[0] -= a[i]
    b[0] //= 2
    for i in range(n-1):
        b[i+1] = a[i] - b[i]
    print(*b)
