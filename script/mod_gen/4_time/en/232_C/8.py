def main():
    n, m = map(int,input().split())
    a = []
    b = []
    c = []
    d = []
    for i in range(m):
        x, y = map(int,input().split())
        a.append(x)
        b.append(y)
    for i in range(m):
        x, y = map(int,input().split())
        c.append(x)
        d.append(y)
    for i in range(n):
        for j in range(n):
            if (i+1 in a and j+1 in b) and (i+1 not in c and j+1 not in d):
                print("No")
                exit()
            elif (i+1 not in a and j+1 not in b) and (i+1 in c and j+1 in d):
                print("No")
                exit()
    print("Yes")

if __name__ == '__main__':
    main()