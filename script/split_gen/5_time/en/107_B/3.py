def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    b = []
    for i in range(h):
        if a[i].count(".") != w:
            b.append(a[i])
    c = []
    for i in range(len(b[0])):
        for j in range(len(b)):
            if b[j][i] == "#":
                break
        else:
            c.append(i)
    for i in range(len(b)):
        for j in range(len(c)):
            b[i] = b[i][:c[j]] + b[i][c[j]+1:]
    for i in range(len(b)):
        print(b[i])
    return 0
