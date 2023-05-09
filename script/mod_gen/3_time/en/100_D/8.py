def main():
    N, M = map(int, input().split())
    cakes = [tuple(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(8):
        vals = [0] * N
        for j in range(N):
            for k in range(3):
                if i & 1 << k:
                    vals[j] += cakes[j][k]
                else:
                    vals[j] -= cakes[j][k]
        vals.sort(reverse=True)
        ans = max(ans, sum(vals[:M]))
    print(ans)

if __name__ == '__main__':
    main()