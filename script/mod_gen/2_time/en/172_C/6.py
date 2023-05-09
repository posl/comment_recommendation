def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(N + 1):
        if i == 0:
            a = 0
        else:
            a = A[i - 1]
        if K - a < 0:
            break
        cnt = i
        k = K - a
        for j in range(M + 1):
            if j == 0:
                b = 0
            else:
                b = B[j - 1]
            if k - b < 0:
                break
            cnt += 1
            k -= b
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()