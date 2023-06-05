def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    count = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i != j:
                if a.count(i) + b.count(i) == a.count(j) + b.count(j) == 0:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()