def solve():
    S = input()
    ans = 0
    cnt = 0
    for s in S:
        if s == 'A' or s == 'C' or s == 'G' or s == 'T':
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0
    print(ans)
    return 0

if __name__ == '__main__':
    solve()