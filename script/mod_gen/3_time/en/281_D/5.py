def main():
    N, K, D = map(int, input().split())
    A = list(map(int, input().split()))
    ans = -1
    for i in range(2 ** N):
        if bin(i).count('1') != K:
            continue
        S = 0
        for j in range(N):
            if (i >> j) & 1:
                S += A[j]
        if S % D == 0:
            ans = max(ans, S)
    print(ans)

if __name__ == '__main__':
    main()