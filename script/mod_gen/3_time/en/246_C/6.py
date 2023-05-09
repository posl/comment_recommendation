def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    ans = 0
    for i in range(N):
        if K > 0:
            K -= 1
            ans += A[i] - X
        else:
            ans += A[i]
    print(max(ans, 0))

if __name__ == '__main__':
    main()