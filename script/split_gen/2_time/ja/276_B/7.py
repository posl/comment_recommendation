def main():
    N, M = map(int, input().split())
    # 都市と道路の隣接リストを作る
    city = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        city[a-1].append(b-1)
        city[b-1].append(a-1)
    # 都市iと直接結ばれている都市の数と、都市iと直接結ばれている都市を出力
    for i in range(N):
        print(len(city[i]), end='')
        for j in city[i]:
            print(' ' + str(j+1), end='')
        print()
