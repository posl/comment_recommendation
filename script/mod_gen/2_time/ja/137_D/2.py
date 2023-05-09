def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for i in range(M):
        for j in range(N):
            if AB[j][0] == i + 1:
                ans += AB[j][1]
                AB[j][0] = 0
    print(ans)
main()

if __name__ == '__main__':
    main()