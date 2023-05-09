def main():
    N, K, Q = map(int, input().split())
    A = [int(input()) for i in range(Q)]
    #print(N, K, Q)
    #print(A)
    #print([K - Q + A.count(i) for i in range(1, N+1)])
    print(*["Yes" if K - Q + A.count(i) > 0 else "No" for i in range(1, N+1)], sep='
')

if __name__ == '__main__':
    main()