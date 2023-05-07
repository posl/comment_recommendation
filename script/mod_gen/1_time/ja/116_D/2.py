def main():
    N, K = map(int, input().split())
    D = []
    for _ in range(N):
        t, d = map(int, input().split())
        D.append((d, t))
    D.sort(reverse=True)
    #print(D)
    ans = 0
    cnt = 0
    S = set()
    for d, t in D[:K]:
        ans += d
        if t not in S:
            cnt += 1
            S.add(t)
    ans += cnt * cnt
    #print(ans)
    for d, t in D[K:]:
        if t in S:
            continue
        S.add(t)
        cnt += 1
        ans += d
        ans += 2 * cnt - 1
        #print(d, cnt, ans)
    print(ans)

if __name__ == '__main__':
    main()