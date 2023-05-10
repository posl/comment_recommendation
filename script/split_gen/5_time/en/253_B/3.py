def main():
    h, w = map(int, input().split())
    s = [input() for i in range(h)]
    c = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                c += 1
    if c == 1:
        print(1)
    elif c == 2:
        print(0)
    else:
        print(c)
