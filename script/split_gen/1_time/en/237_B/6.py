def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    b = [[0 for _ in range(h)] for _ in range(w)]
    for i in range(h):
        for j in range(w):
            b[j][i] = a[i][j]
    for i in range(w):
        print(' '.join(map(str, b[i])))
