def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()
    if n >= m:
        print(0)
        return
    diff = []
    for i in range(1,m):
        diff.append(x[i]-x[i-1])
    diff.sort()
    ans = sum(diff[:m-n])
    print(ans)

if __name__ == '__main__':
    main()