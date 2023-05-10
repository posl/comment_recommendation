def main():
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        a.append(list(map(int,input().split()))[1:])
    ans = 0
    for i in range(m):
        for j in range(n):
            if not i+1 in a[j]:
                break
        else:
            ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()