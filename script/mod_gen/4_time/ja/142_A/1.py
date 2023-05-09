def solve():
    # 解答を返す
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        if i % 2 != 0:
            ans += 1
    print("{:.10f}".format(ans/N))
    return 0

if __name__ == '__main__':
    solve()