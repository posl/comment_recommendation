def main():
    N, M = map(int, input().split())
    cakes = []
    for _ in range(N):
        cakes.append(list(map(int, input().split())))
    max_score = 0
    for i in range(2 ** N):
        # print(i)
        # print(bin(i))
        # print(bin(i)[2:])
        # print(bin(i)[2:].zfill(N))
        # print(list(bin(i)[2:].zfill(N)))
        # print(list(map(int, list(bin(i)[2:].zfill(N)))))
        choice = list(map(int, list(bin(i)[2:].zfill(N))))
        if choice.count(1) != M:
            continue
        score = 0
        for j in range(N):
            if choice[j] == 0:
                continue
            score += abs(cakes[j][0]) + abs(cakes[j][1]) + abs(cakes[j][2])
        max_score = max(max_score, score)
    print(max_score)

if __name__ == '__main__':
    main()