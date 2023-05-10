def solve():
    N = int(input())
    ans = 0
    if N >= 1000:
        ans += N-999
    if N >= 1000000:
        ans += N-999999
    if N >= 1000000000:
        ans += N-999999999
    if N >= 1000000000000:
        ans += N-999999999999
    if N >= 1000000000000000:
        ans += N-999999999999999
    print(ans)
    return 0

if __name__ == '__main__':
    solve()