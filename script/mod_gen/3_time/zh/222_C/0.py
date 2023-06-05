def main():
    N, M = map(int, input().split())
    A = [input() for i in range(2*N)]
    rank = [i for i in range(2*N)]
    for i in range(M):
        rank = sorted(rank, key=lambda x: (-A[x][i], x))
    for i in rank:
        print(i+1)

if __name__ == '__main__':
    main()