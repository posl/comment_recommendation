def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] -= 1
    b = [0] * n
    for i in range(n):
        if a[i] >= 0:
            b[a[i]] += 1
    c = []
    for i in range(n):
        if b[i] == 0:
            c.append(i)
    if len(c) == 0:
        print(-1)
        return
    ans = 0
    for i in range(n):
        if b[i] > 1:
            for j in range(b[i] - 1):
                if len(c) == 0:
                    print(-1)
                    return
                k = c.pop()
                a[k] = i
                ans += 1
    for i in range(n):
        if a[i] < 0:
            a[i] = c.pop()
    print(ans)
    return
main()

if __name__ == '__main__':
    main()