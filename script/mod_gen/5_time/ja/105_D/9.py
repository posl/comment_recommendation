def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = [0] * (N + 1)
    for i in range(N):
        sum_A[i + 1] = sum_A[i] + A[i]
    sum_A = [a % M for a in sum_A]
    cnt = {}
    for a in sum_A:
        if a in cnt:
            cnt[a] += 1
        else:
            cnt[a] = 1
    ans = 0
    for c in cnt.values():
        ans += c * (c - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()