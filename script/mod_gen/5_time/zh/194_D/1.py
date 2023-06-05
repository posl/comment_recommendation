def solve():
    N = int(input())
    ans = 0
    for i in range(1,N):
        ans += 1/i
    ans = ans * N
    print("{:.11f}".format(ans))

if __name__ == '__main__':
    solve()