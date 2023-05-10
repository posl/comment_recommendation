def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))
    b = [0 for i in range(m+1)]
    b[0] = c[0] // a[0]
    for i in range(n+m):
        for j in range(1, min(i+1, m)+1):
            b[j] += c[i+1] * b[j-1]
    print(" ".join(map(str, b)))
