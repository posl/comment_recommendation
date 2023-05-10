def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []
    for i in range(n):
        c.append([a[i]+b[i],a[i],b[i],i+1])
    c.sort(reverse=True)
    ans = []
    for i in range(x):
        ans.append(c[i][3])
    for i in range(x,x+y):
        if c[i][1] > c[i][2]:
            ans.append(c[i][3])
    for i in range(x+y,x+y+z):
        ans.append(c[i][3])
    ans.sort()
    for i in range(len(ans)):
        print(ans[i])

if __name__ == '__main__':
    main()