def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2 * N)]
    ranking = [(i, 0) for i in range(2 * N)]
    for i in range(M):
        for j in range(N):
            id1 = ranking[2 * j][0]
            id2 = ranking[2 * j + 1][0]
            hand1 = A[id1][i]
            hand2 = A[id2][i]
            if hand1 == hand2:
                continue
            if hand1 == "G" and hand2 == "C":
                ranking[2 * j][1] -= 1
            elif hand1 == "C" and hand2 == "P":
                ranking[2 * j][1] -= 1
            elif hand1 == "P" and hand2 == "G":
                ranking[2 * j][1] -= 1
            else:
                ranking[2 * j + 1][1] -= 1
        ranking.sort(key=lambda x: (x[1], x[0]))
    for i in range(2 * N):
        print(ranking[i][0] + 1)

if __name__ == '__main__':
    main()