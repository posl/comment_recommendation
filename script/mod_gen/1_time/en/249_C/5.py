def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(2 ** 26):
        bit = bin(i)[2:].zfill(26)
        cnt = 0
        for s in S:
            for j in s:
                if bit[ord(j) - ord("a")] == "0":
                    break
            else:
                cnt += 1
        if cnt >= K:
            ans = max(ans, bit.count("1"))
    print(ans)

if __name__ == '__main__':
    main()