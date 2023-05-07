def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    p.sort(reverse=True)
    ans = p[0] // 2
    for i in range(1, n):
        ans += p[i]
    print(ans)
