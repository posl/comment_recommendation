def main():
    n,k = map(int,input().split())
    p = [list(map(int,input().split())) for _ in range(n)]
    p.sort(key=lambda x:sum(x),reverse=True)
    p4 = [p[i][0] for i in range(n)]
    p4.sort(reverse=True)
    for i in range(n):
        if p4.index(p[i][0])+1<=k:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()