def main():
    N, Q = map(int, input().split())
    A = [set() for i in range(N)]
    B = [set() for i in range(N)]
    for i in range(Q):
        T, a, b = map(int, input().split())
        if T == 1:
            A[a - 1].add(b - 1)
            B[b - 1].add(a - 1)
        elif T == 2:
            if a - 1 in A[b - 1]:
                A[b - 1].remove(a - 1)
            if b - 1 in B[a - 1]:
                B[a - 1].remove(b - 1)
        else:
            if a - 1 in B[b - 1] and b - 1 in A[a - 1]:
                print('Yes')
            else:
                print('No')

if __name__ == '__main__':
    main()