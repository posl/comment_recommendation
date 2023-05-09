def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    C = [0] * N
    A = [0] * N
    for i in range(N):
        if S[i] == '0':
            C[i] = 1
        else:
            A[i] = 1
    for i in range(1, N):
        C[i] += C[i-1]
        A[i] += A[i-1]
    ans = 0
    for i in range(N):
        ans = max(ans, C[i] + A[N-1] - A[i])
    print(ans)

if __name__ == '__main__':
    main()