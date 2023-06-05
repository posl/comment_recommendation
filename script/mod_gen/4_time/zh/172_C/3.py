def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a_sum = [0]
    b_sum = [0]
    for i in range(N):
        a_sum.append(a_sum[i] + A[i])
    for i in range(M):
        b_sum.append(b_sum[i] + B[i])
    ans = 0
    j = M
    for i in range(N+1):
        if a_sum[i] > K:
            break
        while b_sum[j] > K - a_sum[i]:
            j -= 1
        ans = max(ans, i+j)
    print(ans)

if __name__ == '__main__':
    main()