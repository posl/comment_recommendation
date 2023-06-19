def main():
    n=int(input())
    m=2*n+1
    l=[i for i in range(1,m+1)]
    for i in range(n):
        a=int(input())
        l.remove(a)
        b=max([j for j in l if j<a])
        l.remove(b)
        print(b)
        c=int(input())
        l.remove(c)
        d=max([j for j in l if j<c])
        l.remove(d)
        print(d)
main()
