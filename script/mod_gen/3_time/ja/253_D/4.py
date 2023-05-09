def main():
    N,A,B=map(int,input().split())
    Alist = list(range(0,N+1,A))
    Blist = list(range(0,N+1,B))
    Clist = list(set(Alist+Blist))
    Clist.sort()
    print(sum(Clist))

if __name__ == '__main__':
    main()