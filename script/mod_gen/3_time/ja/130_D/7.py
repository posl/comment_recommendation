def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    #print(N, K, a)
    ans = 0
    right = 0
    total = 0
    for left in range(N):
        while right < N and total < K:
            total += a[right]
            right += 1
        if total >= K:
            ans += N - right + 1
        total -= a[left]
    print(ans)
main()

if __name__ == '__main__':
    main()