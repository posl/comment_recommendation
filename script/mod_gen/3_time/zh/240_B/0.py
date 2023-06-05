def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    ans = 0
    prev = 0
    for i in range(n):
        if a[i] != prev:
            ans += 1
            prev = a[i]
    print(ans)

if __name__ == '__main__':
    main()