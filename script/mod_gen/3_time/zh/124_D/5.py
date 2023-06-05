def main():
    n,k = map(int, input().split())
    s = input()
    #print(n,k,s)
    #print(s)
    a = []
    for i in range(n-1):
        if s[i] != s[i+1]:
            a.append(i)
    #print(a)
    l = len(a)
    if l <= 2*k:
        print(n)
    else:
        #print(a)
        #print(l)
        #print(k)
        b = [0]*(l-2*k+1)
        for i in range(l-2*k+1):
            b[i] = a[i+2*k-1]-a[i]+1
        #print(b)
        print(max(b))

if __name__ == '__main__':
    main()