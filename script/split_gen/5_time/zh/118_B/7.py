def main():
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    #print(a)
    b = []
    for i in range(n):
        for j in range(a[i][0]):
            b.append(a[i][j+1])
    #print(b)
    c = [0]*(m+1)
    for i in range(len(b)):
        c[b[i]] += 1
    #print(c)
    count = 0
    for i in range(len(c)):
        if c[i] == n:
            count += 1
    print(count)
