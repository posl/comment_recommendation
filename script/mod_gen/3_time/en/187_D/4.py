def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    ans = 0
    Aoki = 0
    Takahashi = 0
    for i in range(N):
        Aoki += A[i]
        Takahashi += B[i]
        if A[i] + B[i] > max(Aoki, Takahashi):
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()