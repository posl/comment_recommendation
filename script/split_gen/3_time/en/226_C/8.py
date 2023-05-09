def main():
    N = int(input())
    moves = [tuple(map(int, input().split())) for _ in range(N)]
    moves.sort(key=lambda x: x[0])
    moves.append((0, 0))
    times = [0] * (N + 1)
    for i in range(N):
        t, k, *a = moves[i]
        times[i + 1] = t + max(times[j] for j in a)
    print(times[-1])
