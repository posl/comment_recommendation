def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if M == 0:
            ans += A[i]
        else:
            if A[i] > 2 ** M:
                ans += A[i] - 2 ** M
                A[i] = 2 ** M
            M -= A[i].bit_length() - 1
    print(ans)

if __name__ == '__main__':
    main()