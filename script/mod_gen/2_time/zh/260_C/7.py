def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append([a[i]+b[i],a[i],i+1])
    c.sort(reverse=True)
    print(c)
    ans = []
    for i in range(x):
        ans.append(c[i][2])
    for i in range(x,x+y):
        ans.append(c[i][2])
    for i in range(x+y,x+y+z):
        ans.append(c[i][2])
    ans.sort()
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()