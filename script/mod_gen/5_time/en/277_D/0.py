def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if m == 1:
        print(0)
        return
    if n == 1:
        print(a[0])
        return
    diff = []
    for i in range(n-1):
        diff.append(a[i+1]-a[i])
    diff.sort(reverse=True)
    print(a[-1]+sum(diff[1:]))

if __name__ == '__main__':
    main()