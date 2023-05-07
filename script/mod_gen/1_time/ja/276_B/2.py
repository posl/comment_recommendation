def main():
    N, M = map(int, input().split())
    city = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        city[A-1].append(B)
        city[B-1].append(A)
    for i in range(N):
        city[i].sort()
        print(len(city[i]), *city[i])

if __name__ == '__main__':
    main()