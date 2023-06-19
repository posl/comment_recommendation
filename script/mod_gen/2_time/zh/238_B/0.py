def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    a.append(a[0] + 360)
    a.append(a[1] + 360)
    ans = 0
    for i in range(n):
        ans = max(ans, a[i + 2] - a[i])
    print(360 - ans)

if __name__ == '__main__':
    main()