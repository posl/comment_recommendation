def main():
    N,M = map(int,input().split())
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i],B[i] = map(int,input().split())
    ans = N*(N-1)
    for i in range(M):
        for j in range(i+1,M):
            if A[i] == A[j] and B[i] == B[j]:
                ans -= 1
            elif A[i] == B[j] and B[i] == A[j]:
                ans -= 1
    print(ans)

if __name__ == '__main__':
    main()