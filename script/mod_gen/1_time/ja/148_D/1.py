def main():
    n = int(input())
    a = list(map(int, input().split()))
    
    if n == 1:
        if a[0] == 1:
            print(0)
        else:
            print(-1)
        return
    
    if a[0] != 1:
        print(-1)
        return
    
    i = 1
    ans = 0
    while i < n:
        if a[i] != i + 1:
            ans += 1
        else:
            i += 1
        i += 1
    
    print(ans)

if __name__ == '__main__':
    main()