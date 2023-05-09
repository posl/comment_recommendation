def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    AB.append([M+1, 0])
    ans = 0
    B = []
    for i in range(N+1):
        if AB[i][0] <= M:
            B.append(AB[i][1])
        else:
            break
    B.sort(reverse=True)
    for i in range(M):
        ans += B[i]
    print(ans)

if __name__ == '__main__':
    main()