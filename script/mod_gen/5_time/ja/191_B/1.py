def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    ans = []
    for i in range(n):
        if a[i] == x:
            pass
        else:
            ans.append(a[i])
    print(*ans)

if __name__ == '__main__':
    main()