def solve():
    N = int(input())
    if N == 0:
        print(0)
        return
    ans = ""
    while N != 0:
        if N % (-2) == 0:
            ans += "0"
        else:
            ans += "1"
            N -= 1
        N //= (-2)
    print(ans[::-1])

if __name__ == '__main__':
    solve()