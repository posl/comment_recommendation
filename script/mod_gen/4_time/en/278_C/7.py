def main():
    n,q = map(int,input().split())
    f = [ set() for _ in range(n) ]
    for _ in range(q):
        t,a,b = map(int,input().split())
        if t == 1:
            f[a-1].add(b-1)
        elif t == 2:
            f[a-1].discard(b-1)
        else:
            print("Yes" if b-1 in f[a-1] else "No")

if __name__ == '__main__':
    main()