def main():
    N, M = map(int, input().split())
    cities = []
    for i in range(N):
        cities.append([i+1])
    for i in range(M):
        A, B = map(int, input().split())
        cities[A-1].append(B)
        cities[B-1].append(A)
    for i in range(N):
        cities[i].sort()
        print(len(cities[i])-1, end=" ")
        for j in range(len(cities[i])-1):
            print(cities[i][j+1], end=" ")
        print()

if __name__ == '__main__':
    main()