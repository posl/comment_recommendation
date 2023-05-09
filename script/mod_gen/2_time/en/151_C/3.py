def main():
    n, m = map(int, input().split())
    ac = [False]*n
    wa = [0]*n
    for _ in range(m):
        p, s = input().split()
        p = int(p)-1
        if s == 'AC':
            ac[p] = True
        else:
            if not ac[p]:
                wa[p] += 1
    ans = [0, 0]
    for i in range(n):
        if ac[i]:
            ans[0] += 1
            ans[1] += wa[i]
    print(*ans)

if __name__ == '__main__':
    main()