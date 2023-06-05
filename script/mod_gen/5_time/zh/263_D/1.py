def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] < 0:
            ans += -A[i] * L
        else:
            ans += A[i] * R
    print(ans)

if __name__ == '__main__':
    main()