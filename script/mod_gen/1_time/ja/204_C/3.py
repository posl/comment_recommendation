def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    ans = 0
    for i in range(N):
        ans += (N - 1) * (N - 2) // 2
        for j in range(M):
            if AB[j][0] == i + 1:
                ans -= 1
            if AB[j][1] == i + 1:
                ans -= 1
    print(ans)

if __name__ == '__main__':
    main()