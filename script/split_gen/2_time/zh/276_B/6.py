def main():
    N, M = map(int, input().split())
    cities = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        cities[A-1].append(B)
        cities[B-1].append(A)
    for i in range(N):
        cities[i].sort()
    for i in range(N):
        print(len(cities[i]), end=" ")
        for j in range(len(cities[i])):
            print(cities[i][j], end=" ")
        print()
