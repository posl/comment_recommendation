def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    s = set(c[:k])
    ans = len(s)
    for i in range(n-k):
        s.remove(c[i])
        s.add(c[i+k])
        ans = max(ans, len(s))
    print(ans)
