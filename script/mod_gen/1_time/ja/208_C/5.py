def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    cnt = [0] * N
    for i in range(N):
        cnt[i] = (A[i] - 1) // K
    ans = [0] * N
    for i in range(N):
        ans[i] = cnt[i] + 1
    for i in range(N):
        if i == 0:
            continue
        if cnt[i] == cnt[i - 1]:
            ans[i] = ans[i - 1]
    for i in range(N):
        print(ans[i])

if __name__ == '__main__':
    main()