def main():
    N = int(input())
    S = [input() for _ in range(N)]
    D = {}
    for s in S:
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        if str(d) in D:
            D[str(d)] += 1
        else:
            D[str(d)] = 1
    ans = 0
    for v in D.values():
        ans += v * (v - 1) // 2
    print(ans)

if __name__ == '__main__':
    main()