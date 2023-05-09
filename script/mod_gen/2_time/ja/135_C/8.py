def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    N = int(readline())
    A = list(map(int,readline().split()))
    B = list(map(int,readline().split()))
    ans = 0
    for i in range(N):
        if A[i] >= B[i]:
            ans += B[i]
            A[i] -= B[i]
        else:
            ans += A[i]
            B[i] -= A[i]
            if A[i + 1] >= B[i]:
                ans += B[i]
                A[i + 1] -= B[i]
            else:
                ans += A[i + 1]
                A[i + 1] = 0
    print(ans)

if __name__ == '__main__':
    main()