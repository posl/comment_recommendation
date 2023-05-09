def main():
    n, m = map(int, input().split())
    ans = [0] * n
    pen = [0] * n
    ac = [False] * n
    for _ in range(m):
        p, s = input().split()
        p = int(p) - 1
        if s == 'AC':
            if not ac[p]:
                ac[p] = True
        else:
            if not ac[p]:
                pen[p] += 1
    for i in range(n):
        if ac[i]:
            ans[0] += 1
            ans[1] += pen[i]
    print(*ans)

if __name__ == '__main__':
    main()