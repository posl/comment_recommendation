def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    a.append(a[0])
    ans = 0
    for i in range(n):
        ans = max(ans, a[i] - a[i+1])
    print(360 - ans)

if __name__ == '__main__':
    main()