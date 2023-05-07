def main():
    N, M = map(int, input().split())
    cakes = []
    for i in range(N):
        cakes.append(list(map(int, input().split())))
    ans = 0
    for i in range(2 ** 3):
        score = [0] * N
        for j in range(N):
            for k in range(3):
                if (i >> k) & 1:
                    score[j] += cakes[j][k]
                else:
                    score[j] -= cakes[j][k]
        score.sort(reverse=True)
        ans = max(ans, sum(score[:M]))
    print(ans)

if __name__ == '__main__':
    main()