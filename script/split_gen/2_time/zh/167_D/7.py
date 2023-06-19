def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * n
    b[0] = 1
    for i in range(1, n):
        b[i] = a[b[i-1]-1]
    if k <= n:
        print(b[k-1])
        return
    k = (k - n) % (n - b.index(b[n-1]))
    print(b.index(b[n-1] + k) + 1)
