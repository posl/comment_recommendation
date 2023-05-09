def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1 << 31
    for i in range(N):
        for j in range(i, N):
            x = A[i]
            for k in range(i + 1, j + 1):
                x |= A[k]
            ans = min(ans, x)
    print(ans)

if __name__ == '__main__':
    main()