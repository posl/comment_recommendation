def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    o1 = o2 = None
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                if o1 is None:
                    o1 = (i, j)
                else:
                    o2 = (i, j)
    print(abs(o1[0] - o2[0]) + abs(o1[1] - o2[1]))
