def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    s = sum(p[:k])
    for i in range(k, n):
        s = max(s, s - p[i-k] + p[i])
    print((s + k) / 2)
