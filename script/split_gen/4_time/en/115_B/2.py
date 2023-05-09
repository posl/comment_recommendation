def main():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort(reverse=True)
    ans = 0
    for i in range(N):
        if i == 0:
            ans += p[i] // 2
        else:
            ans += p[i]
    print(ans)
