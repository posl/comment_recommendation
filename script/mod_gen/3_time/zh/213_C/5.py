def main():
    h,w,n = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    for i in range(n):
        a[i] -= 1
        b[i] -= 1
    h1 = []
    w1 = []
    for i in range(n):
        h1.append(a[i])
        w1.append(b[i])
    h1 = list(set(h1))
    w1 = list(set(w1))
    h1.sort()
    w1.sort()
    h2 = {}
    w2 = {}
    for i in range(len(h1)):
        h2[h1[i]] = i
    for i in range(len(w1)):
        w2[w1[i]] = i
    for i in range(n):
        print(h2[a[i]]+1,w2[b[i]]+1)

if __name__ == '__main__':
    main()