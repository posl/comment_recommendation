def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(N, K)
    #print(A)
    #print(A[0])
    a = 0
    b = 0
    for i in range(N):
        if A[i] > K:
            b = i
            break
        else:
            a = i
    #print(a, b)
    if a == N-1:
        for i in range(N):
            print(K)
    else:
        for i in range(N):
            if i < b:
                print(K//N)
            elif i == b:
                print(K//N + K%N)
            else:
                print(0)

if __name__ == '__main__':
    main()