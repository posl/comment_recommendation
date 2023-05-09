def main():
    N, Q = map(int, input().split())
    #print(N, Q)
    A = []
    for i in range(N):
        L = list(map(int, input().split()))
        #print(L)
        A.append(L)
    #print(A)
    for i in range(Q):
        s, t = map(int, input().split())
        #print(s, t)
        print(A[s-1][t])

if __name__ == '__main__':
    main()