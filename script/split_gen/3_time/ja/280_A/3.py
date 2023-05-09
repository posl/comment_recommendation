def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                cnt += 1
    print(cnt)
