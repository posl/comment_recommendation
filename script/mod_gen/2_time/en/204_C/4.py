def main():
    n,m = map(int,input().split())
    a = [0]*m
    b = [0]*m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    
    ans = n*(n-1)
    for i in range(m):
        for j in range(i+1,m):
            if a[i] == a[j] and b[i] == b[j]:
                ans -= 2
            elif a[i] == b[j] and b[i] == a[j]:
                ans -= 2
            elif a[i] == a[j] or a[i] == b[j] or b[i] == a[j] or b[i] == b[j]:
                ans -= 1
    print(ans)
    
main()

if __name__ == '__main__':
    main()