def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    ans = 0
    for i in range(1, n):
        if a[i] <= a[i-1] * 2:
            ans += 1
        else:
            ans = 0
    print(ans)

if __name__ == '__main__':
    main()