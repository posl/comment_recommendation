def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(input())
    hlist = []
    wlist = []
    for i in range(h):
        if a[i].count('#') == 0:
            hlist.append(i)
    for j in range(w):
        if [a[i][j] for i in range(h)].count('#') == 0:
            wlist.append(j)
    for i in range(h):
        if i not in hlist:
            print(''.join([a[i][j] for j in range(w) if j not in wlist]))
