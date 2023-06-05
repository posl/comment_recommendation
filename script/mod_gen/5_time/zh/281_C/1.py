def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)
    ans = 0
    for i in range(n):
        if t < a[i]:
            ans = i
            break
        t -= a[i]
        ans = t // a[i]
        t %= a[i]
    print(ans+1, t)

if __name__ == '__main__':
    main()