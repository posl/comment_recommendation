def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > R:
            ans += R
        elif A[i] < L:
            ans += L
        else:
            ans += A[i]
    print(ans)

if __name__ == '__main__':
    main()