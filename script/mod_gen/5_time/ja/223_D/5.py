def main():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(m)]
    ab = sorted(ab, key=lambda x: x[1])
    ans = [0] * n
    for i in range(m):
        ans[ab[i][1]-1] = ab[i][0]
    if ans[0] == 0:
        ans[0] = 1
    for i in range(n-1):
        if ans[i+1] == 0:
            ans[i+1] = i+2
    for i in range(n-1):
        if ans[i] > ans[i+1]:
            print(-1)
            exit()
    print(*ans)

if __name__ == '__main__':
    main()