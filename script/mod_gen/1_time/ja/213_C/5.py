def main():
    h,w,n = map(int,input().split())
    #print(h,w,n)
    a = [0]*n
    b = [0]*n
    for i in range(n):
        a[i],b[i] = map(int,input().split())
        #print(a[i],b[i])
    #print(a)
    #print(b)
    a = list(set(a))
    a.sort()
    b = list(set(b))
    b.sort()
    #print(a)
    #print(b)
    for i in range(n):
        print(a.index(a[i])+1,b.index(b[i])+1)

if __name__ == '__main__':
    main()