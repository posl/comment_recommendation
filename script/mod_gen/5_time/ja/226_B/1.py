def main():
    n = int(input())
    #print(n)
    l = []
    for i in range(n):
        #print(i)
        l.append(list(map(int,input().split())))
    #print(l)
    l.sort()
    #print(l)
    ans = 1
    for i in range(n-1):
        if l[i] != l[i+1]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()