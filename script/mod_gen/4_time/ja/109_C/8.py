def main():
    n, x = map(int, input().split())
    x_list = list(map(int, input().split()))
    x_list.append(x)
    x_list.sort()
    diffs = []
    for i in range(1, n+1):
        diffs.append(abs(x_list[i] - x_list[i-1]))
    ans = diffs[0]
    for i in range(1, n):
        ans = gcd(ans, diffs[i])
    print(ans)

if __name__ == '__main__':
    main()