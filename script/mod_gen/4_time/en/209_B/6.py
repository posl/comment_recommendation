def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 'Yes'
    for i in range(n):
        if i % 2 == 1:
            a[i] -= 1
        x -= a[i]
        if x < 0:
            ans = 'No'
            break
    print(ans)

if __name__ == '__main__':
    main()