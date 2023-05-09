def main():
    n = int(input())
    snuke = []
    for i in range(n):
        t, x, a = map(int, input().split())
        snuke.append((t, x, a))
    snuke.sort()
    ans = 0
    for t, x, a in snuke:
        if t >= x:
            ans += a
    print(ans)

if __name__ == '__main__':
    main()