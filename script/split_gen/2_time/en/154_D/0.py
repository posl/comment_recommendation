def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    s = sum(p[:k])
    m = s
    for i in range(n-k):
        s = s + p[k+i] - p[i]
        m = max(m, s)
    print(m/2+k/2)
