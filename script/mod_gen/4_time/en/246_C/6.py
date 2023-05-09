def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [0] + A
    ans = 0
    for i in range(N):
        if A[i+1] - A[i] > X:
            ans += (A[i+1] - A[i]) // X
            if (A[i+1] - A[i]) % X == 0:
                ans -= 1
    if ans <= K:
        print(0)
    else:
        print(ans - K)

if __name__ == '__main__':
    main()