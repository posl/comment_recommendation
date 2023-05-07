def main():
    n = int(input())
    w = list(map(int, input().split()))
    s1 = sum(w)
    s2 = 0
    ans = 1000
    for i in range(n-1):
        s1 -= w[i]
        s2 += w[i]
        ans = min(ans, abs(s1-s2))
    print(ans)
