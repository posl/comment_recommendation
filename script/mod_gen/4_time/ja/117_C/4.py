def main():
    n,m = map(int,input().split())
    x = list(map(int,input().split()))
    x.sort()
    if n >= m:
        print(0)
        return
    diff = []
    for i in range(m-1):
        diff.append(x[i+1]-x[i])
    diff.sort(reverse=True)
    print(sum(diff[n-1:]))

if __name__ == '__main__':
    main()