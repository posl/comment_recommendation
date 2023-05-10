def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i]
    if L < 0 and R > 0:
        for i in range(N):
            if A[i] < 0:
                if abs(A[i]) - abs(L) < 0:
                    ans += abs(A[i]) - abs(L)
                    A[i] = L
                else:
                    ans += abs(A[i]) - abs(R)
                    A[i] = R
    elif L < 0 and R <= 0:
        for i in range(N):
            if A[i] < 0:
                ans += abs(A[i]) - abs(L)
                A[i] = L
    elif L >= 0 and R > 0:
        for i in range(N):
            if A[i] > 0:
                ans += abs(A[i]) - abs(R)
                A[i] = R
    print(ans)
main()

if __name__ == '__main__':
    main()