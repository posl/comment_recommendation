def main():
    n,k = map(int,input().split())
    d = []
    a = []
    for i in range(k):
        d.append(int(input()))
        a.append(list(map(int,input().split())))
    l = []
    for i in range(k):
        for j in range(d[i]):
            l.append(a[i][j])
    l = list(set(l))
    print(n-len(l))
