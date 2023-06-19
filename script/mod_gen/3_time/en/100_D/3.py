def main():
    N, M = map(int, input().split())
    ABC = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(2 ** 3):
        tmp = []
        for j in range(N):
            s = 0
            for k in range(3):
                if i >> k & 1:
                    s += ABC[j][k]
                else:
                    s -= ABC[j][k]
            tmp.append(s)
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))
    print(ans)
main()
