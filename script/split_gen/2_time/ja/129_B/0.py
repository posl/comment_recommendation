def main():
    n = int(input())
    w = list(map(int, input().split()))
    s1 = 0
    s2 = sum(w)
    ans = s2
    for i in range(n-1):
        s1 += w[i]
        s2 -= w[i]
        ans = min(abs(s1-s2), ans)
    print(ans)
