def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    A = [A[i] for i in range(N)]
    B = [B[i] for i in range(N)]
    print(A)
    print(B)
    C = [B[i] - A[i] for i in range(N)]
    print(C)
    D = sorted(C)
    print(D)
    E = [D[i] - i for i in range(N)]
    print(E)
    if min(E) >= 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()