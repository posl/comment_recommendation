def main():
    h, w = map(int, input().split())
    a = [input() for _ in range(h)]
    b = []
    for i in range(h):
        if a[i].count('.') != w:
            b.append(a[i])
    c = []
    for i in range(len(b[0])):
        if ''.join([b[j][i] for j in range(len(b))]).count('.') != len(b):
            c.append(''.join([b[j][i] for j in range(len(b))]))
    for i in range(len(c)):
        print(c[i])
