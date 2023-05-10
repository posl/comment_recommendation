def solve():
    N = int(input())
    ans = N
    for i in range(2, int(N ** 0.5) + 1):
        num = i * i
        while num <= N:
            ans -= 1
            num *= i
    print(ans)

if __name__ == '__main__':
    solve()