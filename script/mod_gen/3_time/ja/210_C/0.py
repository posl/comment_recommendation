def main():
    N, K = map(int, input().split())
    c = list(map(int, input().split()))
    cnt = [0] * 10**9
    ans = 0
    for i in range(K):
        cnt[c[i]-1] += 1
    for i in range(N-K):
        cnt[c[i]-1] -= 1
        cnt[c[i+K]-1] += 1
        ans = max(ans, len([x for x in cnt if x > 0]))
    print(ans)

if __name__ == '__main__':
    main()