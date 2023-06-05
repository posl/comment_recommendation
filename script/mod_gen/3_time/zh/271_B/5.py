def main():
    n,q = list(map(int,input().split()))
    a = []
    for i in range(n):
        a.append(list(map(int,input().split())))
    s = []
    for i in range(q):
        s.append(list(map(int,input().split())))
    for i in range(q):
        print(a[s[i][0]-1][s[i][1]-1])

if __name__ == '__main__':
    main()