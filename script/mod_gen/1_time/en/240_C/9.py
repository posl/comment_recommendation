def main():
    n, x = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    ans = 'No'
    for i in range(n):
        x -= a[i][0]
        if x < 0:
            ans = 'No'
            break
        if x == 0:
            ans = 'Yes'
            break
        x += a[i][1]
    print(ans)

if __name__ == '__main__':
    main()