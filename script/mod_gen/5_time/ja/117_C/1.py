def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x = sorted(x)
    if n >= m:
        print(0)
        exit()
    x_diff = []
    for i in range(m-1):
        x_diff.append(x[i+1]-x[i])
    x_diff = sorted(x_diff)
    ans = 0
    for i in range(m-n):
        ans += x_diff[i]
    print(ans)

if __name__ == '__main__':
    main()