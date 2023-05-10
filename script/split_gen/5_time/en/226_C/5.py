def main():
    n = int(input())
    moves = []
    for i in range(n):
        moves.append([int(x) for x in input().split()])
    moves = sorted(moves, key=lambda x: x[0])
    times = [0 for _ in range(n)]
    for i in range(n):
        move = moves[i]
        time = move[0]
        pre = 0
        for j in range(1, len(move)):
            pre = max(pre, times[move[j] - 1])
        times[i] = time + pre
    print(times[-1])
