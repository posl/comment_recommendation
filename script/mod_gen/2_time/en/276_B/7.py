def main():
    N, M = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(M)]
    roads.sort()
    ans = [0 for _ in range(N)]
    for i in range(M):
        ans[roads[i][0]-1] += 1
        ans[roads[i][1]-1] += 1
    for i in range(N):
        print(ans[i], end=' ')
        for j in range(M):
            if roads[j][0] == i+1:
                print(roads[j][1], end=' ')
            elif roads[j][1] == i+1:
                print(roads[j][0], end=' ')
        print()

if __name__ == '__main__':
    main()