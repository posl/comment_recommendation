def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for i in range(Q)]
    print(A, BC)
    B = [BC[i][0] for i in range(Q)]
    C = [BC[i][1] for i in range(Q)]
    print(B, C)
    print(A)
    for i in range(Q):
        A = list(map(lambda x:x if x != B[i] else C[i], A))
        print(A)
        print(sum(A))

if __name__ == '__main__':
    main()