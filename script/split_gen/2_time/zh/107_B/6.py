def main():
    h,w = map(int,input().split())
    a = []
    for i in range(h):
        a.append(input())
    b = []
    for i in range(h):
        if not a[i] == "."*w:
            b.append(a[i])
    c = []
    for i in range(w):
        flag = True
        for j in range(len(b)):
            if b[j][i] == "#":
                flag = False
                break
        if flag:
            c.append(i)
    for i in range(len(b)):
        for j in range(len(c)):
            print(b[i][c[j]],end="")
        print()
