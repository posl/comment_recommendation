def main():
    n = int(input())
    l = []
    r = []
    for i in range(n):
        x,y = map(int,input().split())
        l.append(x)
        r.append(y)
    l.sort()
    r.sort()
    print(l[0],r[-1])

if __name__ == '__main__':
    main()