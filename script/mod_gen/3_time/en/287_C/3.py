def main():
    n,m=map(int,input().split())
    if m!=n-1:
        print("No")
        return
    s=set()
    for _ in range(m):
        u,v=map(int,input().split())
        s.add(u)
        s.add(v)
    if len(s)!=n:
        print("No")
        return
    print("Yes")
    return

if __name__ == '__main__':
    main()