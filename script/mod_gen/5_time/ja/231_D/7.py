def main():
    n,m=map(int, input().split())
    a=[]
    b=[]
    for _ in range(m):
        ai,bi=map(int, input().split())
        a.append(ai)
        b.append(bi)
    a.sort()
    b.sort()
    if a[0]==1 and b[-1]==n:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")

if __name__ == '__main__':
    main()