def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(M)]
    for i in range(M):
        AB[i][0] -= 1
        AB[i][1] -= 1
        CD[i][0] -= 1
        CD[i][1] -= 1
    for i in range(N):
        for j in range(i + 1, N):
            A = [0] * N
            B = [0] * N
            for k in range(M):
                if AB[k][0] == i and AB[k][1] == j:
                    A[k] = 1
                if AB[k][0] == j and AB[k][1] == i:
                    A[k] = 1
                if CD[k][0] == i and CD[k][1] == j:
                    B[k] = 1
                if CD[k][0] == j and CD[k][1] == i:
                    B[k] = 1
            if A != B:
                print('No')
                return
    print('Yes')

if __name__ == '__main__':
    main()