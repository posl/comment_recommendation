def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    BC = []
    for _ in range(Q):
        BC.append(list(map(int,input().split())))
    B = [x[0] for x in BC]
    C = [x[1] for x in BC]
    S = sum(A)
    for i in range(N):
        if A[i] in B:
            S += C[B.index(A[i])]-A[i]
        print(S)

if __name__ == '__main__':
    main()