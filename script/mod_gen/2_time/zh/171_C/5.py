def main():
    N,K=map(int,input().split())
    p=list(map(int,input().split()))
    p.sort()
    print(sum(p[0:K]))

if __name__ == '__main__':
    main()