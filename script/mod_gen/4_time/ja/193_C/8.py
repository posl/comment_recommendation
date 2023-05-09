def solve():
    N = int(input())
    ans = N
    # 2^60 > 10^10
    for i in range(2, 60):
        for j in range(2, 60):
            if i ** j <= N:
                ans -= 1
            else:
                break
    print(ans)

if __name__ == '__main__':
    solve()