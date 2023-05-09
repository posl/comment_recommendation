def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N * N)
        return
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB.sort()
    ans = 0
    for i in range(M):
        for j in range(i + 1, M):
            if AB[i][1] < AB[j][0]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()