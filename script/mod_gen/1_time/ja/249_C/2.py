def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(2 ** N):
        bit = bin(i)[2:].zfill(N)
        if bit.count("1") != K:
            continue
        s = set()
        for j, b in enumerate(bit):
            if b == "1":
                s |= set(S[j])
        ans = max(ans, len(s))
    print(ans)

if __name__ == '__main__':
    main()