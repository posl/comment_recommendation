def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    if a[-1] % 2 == 1:
        print(-1)
        return
    
    for i in range(n):
        if a[i] % 2 == 1:
            continue
        if a[i] * 2 == a[-1]:
            continue
        if a[i] * 2 in a:
            print(a[-1])
            return
    print(-1)

if __name__ == '__main__':
    main()