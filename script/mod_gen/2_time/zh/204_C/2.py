def main():
    n,m = map(int,input().split())
    l = [list(map(int,input().split())) for i in range(m)]
    s = set()
    for i in range(m):
        s.add(l[i][0])
        s.add(l[i][1])
    print(len(s)*(len(s)-1))

if __name__ == '__main__':
    main()