def main():
    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort()
    ans = k
    for i in range(n):
        if ans < ab[i][0]:
            break
        ans += ab[i][1]
    print(ans)
