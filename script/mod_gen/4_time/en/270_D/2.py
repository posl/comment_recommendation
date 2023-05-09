def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(K):
        if A[i] <= N:
            ans += A[i]
            N -= A[i]
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()