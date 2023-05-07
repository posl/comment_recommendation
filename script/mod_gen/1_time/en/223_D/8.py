def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = [-1] * N
    for i in range(N):
        ans[i] = i + 1
    for i in range(M):
        if AB[i][0] > AB[i][1]:
            ans = [-1]
            break
        else:
            ans[AB[i][0] - 1], ans[AB[i][1] - 1] = ans[AB[i][1] - 1], ans[AB[i][0] - 1]
    print(*ans)

if __name__ == '__main__':
    main()