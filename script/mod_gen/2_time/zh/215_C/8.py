def solve():
    s, k = input().split(' ')
    k = int(k)
    s = sorted(s)
    n = len(s)
    if n == 1:
        print(s[0])
        return
    num = 1
    for i in range(1, n):
        num *= i
    ans = ''
    while n > 1:
        index = (k - 1) // num
        ans += s[index]
        del s[index]
        k = k % num
        num = num // (n - 1)
        n -= 1
    ans += s[0]
    print(ans)

if __name__ == '__main__':
    solve()