def main():
    N, M = map(int, input().split())
    # 都市と道路の関係をリストで保持
    roads = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        roads[a - 1].append(b - 1)
        roads[b - 1].append(a - 1)
    # 都市と道路の関係を出力
    for i in range(N):
        print(len(roads[i]) + 1, end = ' ')
        for j in range(len(roads[i])):
            print(roads[i][j] + 1, end = ' ')
        print()

if __name__ == '__main__':
    main()