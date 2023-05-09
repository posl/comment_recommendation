def main():
    #input
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    #calc
    ans = 0
    while max(A) > min(A) + K:
        ans += 1
        for i in range(N):
            if A[i] == max(A):
                for j in range(K):
                    if i+j < N:
                        A[i+j] = max(A)
    #output
    print(ans)

if __name__ == '__main__':
    main()