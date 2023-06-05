def main():
    n = int(input())
    snuke = []
    for i in range(n):
        t, x, a = map(int, input().split())
        snuke.append((t, x, a))
    snuke.sort()
    ans = 0
    for i in range(n):
        t, x, a = snuke[i]
        if x == 0:
            ans += a
        elif x == 1:
            if snuke[i - 1][1] == 0:
                ans += a
            else:
                ans += max(a - snuke[i - 1][2], 0)
        elif x == 2:
            if i + 1 < n and snuke[i + 1][1] == 3:
                ans += max(a - snuke[i + 1][2], 0)
            else:
                ans += a
        elif x == 3:
            if i + 1 < n and snuke[i + 1][1] == 2:
                ans += max(a - snuke[i + 1][2], 0)
            else:
                ans += a
        else:
            if i + 1 < n and snuke[i + 1][1] == 1:
                ans += max(a - snuke[i + 1][2], 0)
            else:
                ans += a
    print(ans)

if __name__ == '__main__':
    main()