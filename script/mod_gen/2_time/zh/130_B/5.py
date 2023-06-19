def main():
    n, x = map(int, input().split())
    l = list(map(int, input().split()))
    d = 0
    ans = 1
    for i in range(n):
        d += l[i]
        if d > x:
            break
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()