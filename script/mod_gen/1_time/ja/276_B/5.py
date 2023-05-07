def main():
    N, M = map(int, input().split())
    # 都市iと道路で直接結ばれた都市を格納するリスト
    city = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        city[A - 1].append(B - 1)
        city[B - 1].append(A - 1)
    for i in range(N):
        city[i].sort()
        print(len(city[i]), end=" ")
        for j in city[i]:
            print(j + 1, end=" ")
        print()

if __name__ == '__main__':
    main()