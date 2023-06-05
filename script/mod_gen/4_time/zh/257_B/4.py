def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    for i in range(q):
        if a[l[i]-1] < n:
            if a[l[i]-1]+1 in a:
                pass
            else:
                a[l[i]-1] += 1
    for i in range(k):
        print(a[i],end = ' ')

if __name__ == '__main__':
    main()