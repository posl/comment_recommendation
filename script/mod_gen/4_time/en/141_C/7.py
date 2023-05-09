def main():
    N,K,Q = map(int,input().split())
    A = [int(input()) for i in range(Q)]
    P = [K-Q]*N
    for i in range(Q):
        P[A[i]-1] += 1
    for i in range(N):
        if P[i] > 0:
            print("Yes")
        else:
            print("No")
main()

if __name__ == '__main__':
    main()