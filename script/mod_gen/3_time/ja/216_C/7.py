def solve():
    N = int(input())
    ans = ''
    while N > 0:
        if N % 2 == 0:
            ans = 'B' + ans
            N //= 2
        else:
            ans = 'A' + ans
            N -= 1
    print(ans)

if __name__ == '__main__':
    solve()