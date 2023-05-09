def main():
    #input
    N, M = map(int, input().split())
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    #count
    ans = 0
    for i in range(M):
        ans += N-1
        for j in range(M):
            if A[i] == B[j]:
                ans -= 1
            if B[i] == A[j]:
                ans -= 1
    #output
    print(ans)

if __name__ == '__main__':
    main()