def main():
    N, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    dist = [0] * N
    for i in range(N):
        for j in range(i + 1, N):
            if i < X < j < Y:
                d = min(j - i, Y - i + j - X + 1)
            elif i < X < Y < j:
                d = min(j - i, Y - i + j - X + 1)
            elif X < i < j < Y:
                d = min(j - i, Y - i + j - X + 1)
            elif X < i < Y < j:
                d = min(j - i, Y - i + j - X + 1)
            elif X < i < j < Y:
                d = min(j - i, Y - i + j - X + 1)
            elif X < i < Y < j:
                d = min(j - i, Y - i + j - X + 1)
            elif i < X < j < Y:
                d = min(j - i, Y - i + j - X + 1)
            elif i < X < Y < j:
                d = min(j - i, Y - i + j - X + 1)
            else:
                d = j - i
            dist[d] += 1
    for k in range(1, N):
        print(dist[k])
