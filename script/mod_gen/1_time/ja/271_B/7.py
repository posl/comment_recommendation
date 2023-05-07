def main():
    #入力
    N, Q = map(int, input().split())
    A = []
    for i in range(N):
        L = list(map(int, input().split()))
        A.append(L)
    #print(A)
    B = []
    for i in range(Q):
        s, t = map(int, input().split())
        B.append(s)
        B.append(t)
    #print(B)
    for i in range(Q):
        print(A[B[2*i]-1][B[2*i+1]])

if __name__ == '__main__':
    main()