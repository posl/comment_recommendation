def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if (i+1) < h and (j+1) < w:
                if a[i][j] + a[i+1][j+1] > a[i+1][j] + a[i][j+1]:
                    print('No')
                    exit()
    print('Yes')
