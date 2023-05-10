def main():
    N, M = map(int, input().split())
    LRs = [tuple(map(int, input().split())) for _ in range(M)]
    LRs.sort(key=lambda x: x[0])
    maxR = LRs[0][1]
    ans = 1
    for L, R in LRs[1:]:
        if L > maxR:
            ans += 1
            maxR = R
        else:
            maxR = max(maxR, R)
    print(ans)

if __name__ == '__main__':
    main()