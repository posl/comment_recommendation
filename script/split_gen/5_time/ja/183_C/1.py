def main():
    n,k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in range(1,n):
        ans += t[0][i]
    print(ans)
    return
