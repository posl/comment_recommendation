def main():
    N = int(input())
    moves = [list(map(int, input().split())) for _ in range(N)]
    moves = sorted(moves, key=lambda x: x[0])
    moves.reverse()
    # print(moves)
    # print(moves[0][0])
    sum = 0
    for i in range(N):
        if i == 0:
            sum += moves[i][0]
        else:
            if moves[i][0] == moves[i-1][0]:
                sum += moves[i][0]
            else:
                sum += moves[i][0] - moves[i][1]
    print(sum)

if __name__ == '__main__':
    main()