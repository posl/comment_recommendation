def main():
    N, M, T = map(int, input().split())
    cafe = []
    for i in range(M):
        A, B = map(int, input().split())
        cafe.append((A, B))
    cafe = sorted(cafe, key=lambda x:x[0])
    battery = N
    battery -= cafe[0][0]
    if battery <= 0:
        print('No')
        return
    for i in range(M):
        if i == M-1:
            battery -= (T - cafe[i][1])
        else:
            battery -= (cafe[i+1][0] - cafe[i][1])
        if battery <= 0:
            print('No')
            return
        battery += (cafe[i+1][0] - cafe[i][0])
        if battery > N:
            battery = N
    print('Yes')

if __name__ == '__main__':
    main()