def main():
    n = int(input())
    w = list(map(int, input().split()))
    s1 = 0
    s2 = sum(w)
    ans = s2
    for i in range(n):
        s1 += w[i]
        s2 -= w[i]
        ans = min(ans, abs(s1 - s2))
    print(ans)
