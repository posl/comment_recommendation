def main():
    N, Q = map(int, input().split())
    F = [[0] * N for _ in range(N)]
    for i in range(Q):
        T, A, B = map(int, input().split())
        A -= 1
        B -= 1
        if T == 1:
            F[A][B] = 1
        elif T == 2:
            F[B][A] = 1
            for j in range(N):
                if F[j][A] == 1:
                    F[j][B] = 1
        else:
            if F[A][B] == 1:
                print('Yes')
            else:
                print('No')

if __name__ == '__main__':
    main()