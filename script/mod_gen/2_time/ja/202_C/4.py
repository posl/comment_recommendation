def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B_C = {}
    for i in range(N):
        if B[i] in B_C:
            B_C[B[i]] += 1
        else:
            B_C[B[i]] = 1
    C_A = {}
    for i in range(N):
        if C[i] in C_A:
            C_A[C[i]] += 1
        else:
            C_A[C[i]] = 1
    ans = 0
    for i in range(N):
        if A[i] in B_C and C[i] in C_A:
            ans += B_C[A[i]] * C_A[C[i]]
    print(ans)

if __name__ == '__main__':
    main()