def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    m = 0
    for i in range(1, n):
        if h[i] <= h[i-1]:
            m += 1
        else:
            ans = max(ans, m)
            m = 0
    ans = max(ans, m)
    print(ans)

if __name__ == '__main__':
    main()