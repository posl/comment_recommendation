def main():
    N, M = map(int, input().split())
    cakes = []
    for _ in range(N):
        cakes.append(list(map(int, input().split())))
    ans = 0
    for i in range(8):
        tmp = [0] * N
        for j in range(N):
            for k in range(3):
                if i & (1 << k):
                    tmp[j] += cakes[j][k]
                else:
                    tmp[j] -= cakes[j][k]
        tmp.sort(reverse=True)
        ans = max(ans, sum(tmp[:M]))
    print(ans)

if __name__ == '__main__':
    main()