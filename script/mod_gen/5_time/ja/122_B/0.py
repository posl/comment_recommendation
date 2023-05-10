def solve():
    s = input()
    ans = 0
    cnt = 0
    for c in s:
        if c in 'ACGT':
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0
    print(ans)

if __name__ == '__main__':
    solve()