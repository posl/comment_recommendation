def main():
    H, W = map(int, input().split())
    #print(H, W)
    a = []
    for i in range(H):
        a.append(input())
    #print(a)
    for i in range(len(a)):
        if a[i] == "." * W:
            a[i] = ""
    #print(a)
    b = []
    for i in range(W):
        b.append("")
    #print(b)
    for i in range(H):
        for j in range(W):
            b[j] += a[i][j]
    #print(b)
    for i in range(len(b)):
        if b[i] == "." * H:
            b[i] = ""
    #print(b)
    c = []
    for i in range(len(b)):
        if b[i] != "":
            c.append(b[i])
    #print(c)
    for i in range(len(c)):
        print(c[i])
