def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B_C = [0] * (N + 1)
    for i in range(N):
        B_C[C[i]] += 1
    B_C_S = [0] * (N + 1)
    for i in range(1, N + 1):
        B_C_S[i] = B_C_S[i - 1] + B_C[i]
    ans = 0
    for i in range(N):
        ans += B_C_S[B[A[i]]]
    print(ans)

if __name__ == '__main__':
    main()