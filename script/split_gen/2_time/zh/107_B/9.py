def main():
    H, W = map(int, input().split())
    a = []
    for i in range(H):
        a.append(input())
    b = []
    for i in range(H):
        if a[i].count("#") != 0:
            b.append(a[i])
    c = []
    for i in range(W):
        tmp = ""
        for j in range(len(b)):
            tmp += b[j][i]
        if tmp.count("#") != 0:
            c.append(tmp)
    for i in range(len(c)):
        print(c[i])
