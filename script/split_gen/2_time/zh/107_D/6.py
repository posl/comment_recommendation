def main():
    N = int(input())
    a = list(map(int,input().split()))
    b = []
    for i in range(N):
        for j in range(i,N):
            b.append(a[i:j+1])
    c = []
    for i in range(len(b)):
        b[i].sort()
        c.append(b[i][len(b[i])//2])
    c.sort()
    print(c[len(c)//2])
main()
