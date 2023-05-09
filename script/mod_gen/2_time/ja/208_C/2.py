def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = [0] * N
    for i in range(N):
        if K >= N - i:
            ans[i] = K // (N - i)
            K -= ans[i] * (N - i)
    for i in range(N):
        if K > 0 and A[i] >= ans[i]:
            ans[i] += 1
            K -= 1
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()