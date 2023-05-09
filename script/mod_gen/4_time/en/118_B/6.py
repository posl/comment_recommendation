def main():
    n, m = map(int, input().split())
    ans = 0
    for i in range(n):
        k, *a = map(int, input().split())
        for j in range(m):
            if j+1 in a:
                ans += 1
                break
    print(m - ans)

if __name__ == '__main__':
    main()