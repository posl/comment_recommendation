def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(1 << N):
        T = []
        for j in range(N):
            if i >> j & 1:
                T.append(S[j])
        if len(T) != K:
            continue
        cnt = 0
        for c in range(26):
            for t in T:
                if chr(c + 97) in t:
                    cnt += 1
                    break
        if cnt == K:
            ans = max(ans, len(T))
    print(ans)

if __name__ == '__main__':
    main()