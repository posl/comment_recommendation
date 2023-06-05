def main():
    n,x,y,z = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = [(a[i],b[i],i+1) for i in range(n)]
    c.sort(key=lambda x:(x[0],x[2]),reverse=True)
    c = c[:x]
    c.sort(key=lambda x:(x[1],x[2]),reverse=True)
    c = c[:x+y]
    c.sort(key=lambda x:(x[0]+x[1],x[2]),reverse=True)
    c = c[:x+y+z]
    c.sort(key=lambda x:x[2])
    for i in c:
        print(i[2])

if __name__ == '__main__':
    main()