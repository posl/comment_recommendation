def main():
    n = int(input())
    w = list(map(int, input().split()))
    s = sum(w)
    ans = s
    for i in range(n):
        s1 = sum(w[:i+1])
        s2 = s - s1
        ans = min(ans, abs(s1-s2))
    print(ans)
