def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M, A)
    S = [0]
    for a in A:
        S.append((S[-1] + a) % M)
    #print(S)
    from collections import defaultdict
    d = defaultdict(int)
    for s in S:
        d[s] += 1
    #print(d)
    ans = 0
    for v in d.values():
        ans += v * (v-1) // 2
    print(ans)

if __name__ == '__main__':
    main()