def main():
    n,k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    p.reverse()
    ans = 0
    for i in range(k):
        ans += p[i]
    ans += k
    ans /= 2
    print(ans)
