def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    #print(n,k,a)
    #print(a)
    for i in range(k):
        a = a[a[i]-1:] + a[:a[i]-1]
        #print(a)
    print(a[0])

if __name__ == '__main__':
    main()