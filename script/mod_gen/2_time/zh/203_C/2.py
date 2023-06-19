def main():
    n,k = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    #print(a)
    #print(b)
    #print(k)
    #print(n)
    i = 0
    while k > 0:
        #print(a[i])
        if k >= a[i]:
            k -= a[i]
            k += b[i]
            i += 1
        else:
            break
        if i == n:
            break
    print(k)

if __name__ == '__main__':
    main()