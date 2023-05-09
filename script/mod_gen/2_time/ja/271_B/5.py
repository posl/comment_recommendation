def main():
    N, Q = map(int, input().split())
    A = []
    for i in range(N):
        L = list(map(int, input().split()))
        A.append(L)
    
    for i in range(Q):
        s, t = map(int, input().split())
        print(A[s-1][t])

if __name__ == '__main__':
    main()