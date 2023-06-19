def main():
    n,m = map(int,raw_input().split())
    a = map(int,raw_input().split())
    a.sort()
    a.reverse()
    #print a
    num = []
    for i in range(m):
        if i == 0:
            for j in range(a[i]):
                num.append(i+1)
        else:
            for j in range(a[i]-a[i-1]):
                num.append(i+1)
    #print num
    ans = []
    for i in range(n):
        if i == 0:
            ans.append(num[0])
        else:
            ans.append(num[i%len(num)])
    #print ans
    for i in range(len(ans)):
        print ans[i],
    print ''

if __name__ == '__main__':
    main()