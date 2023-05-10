def solve():
    # 解答をここに書く
    a, b, k = map(int, input().split())
    ans = ""
    while a > 0 or b > 0:
        if a == 0:
            ans += "b"
            b -= 1
            continue
        if b == 0:
            ans += "a"
            a -= 1
            continue
        if k <= ncr(a + b - 1, b):
            ans += "a"
            a -= 1
        else:
            ans += "b"
            k -= ncr(a + b - 1, b)
            b -= 1
    print(ans)

if __name__ == '__main__':
    solve()