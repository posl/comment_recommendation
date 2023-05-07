def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    B = [0] * (N+1)
    for i in range(N):
        B[A[i]] += 1
    #print(B)
    C = [0] * (N+1)
    for i in range(1, N+1):
        if B[i] > 1:
            C[i] = B[i] * (B[i]-1) // 2
    #print(C)
    for i in range(N):
        ans = 0
        ans += C[A[i]]
        ans -= B[A[i]] - 1
        print(ans)

if __name__ == '__main__':
    main()