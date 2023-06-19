def main():
    n,x,y = map(int,input().split())
    a = list(map(int,input().split()))
    #print(n,x,y)
    #print(a)
    for i in range(n):
        for j in range(i+1,n):
            if i!=j:
                if (x-a[i])**2+(y-a[j])**2 == a[i]**2+a[j]**2:
                    print("Yes")
                    return
    print("No")
    return

if __name__ == '__main__':
    main()