def main():
    N, M = map(int, input().split())
    k = []
    s = []
    p = []
    for _ in range(M):
        k.append(list(map(int, input().split())))
        s.append(k[-1][1:])
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2**N):
        state = [0]*M
        for j in range(N):
            if ((i >> j) & 1):
                for l in range(M):
                    if (j+1) in s[l]:
                        state[l] += 1
        for m in range(M):
            state[m] %= 2
        if state == p:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()