def main():
    h, w = map(int, input().split())
    c = [input() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#':
                break
        else:
            c[i] = ''
    for j in range(w):
        for i in range(h):
            if c[i][j] == '#':
                break
        else:
            for i in range(h):
                c[i] = c[i][:j] + c[i][j+1:]
    for i in range(h):
        print(c[i])
