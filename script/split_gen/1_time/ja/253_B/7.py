def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    i1, j1, i2, j2 = 0, 0, 0, 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                if i1 == 0 and j1 == 0:
                    i1, j1 = i, j
                else:
                    i2, j2 = i, j
    print(abs(i1 - i2) + abs(j1 - j2))
