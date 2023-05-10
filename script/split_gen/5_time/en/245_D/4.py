def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = [0]*(m+1)
    for i in range(m+1):
        b[i] = c[n+m-i]
        for j in range(n+1):
            b[i] -= a[j]*c[n+m-i-j]
    print(*b)
