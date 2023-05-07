def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(M):
        ans += N - 1
        for j in range(M):
            if AB[i][0] == AB[j][1]:
                ans -= 1
    print(ans)

if __name__ == '__main__':
    main()