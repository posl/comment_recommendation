def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a % M for a in A]
    A = [0] + A
    for i in range(1, N+1):
        A[i] += A[i-1]
        A[i] %= M
    cnt = [0] * M
    for a in A:
        cnt[a] += 1
    ans = 0
    for c in cnt:
        ans += c * (c-1) // 2
    print(ans)
main()

if __name__ == '__main__':
    main()