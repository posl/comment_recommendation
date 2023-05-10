def main():
    # input
    N = int(input())
    # compute
    ans = 0
    if N >= 10**3:
        ans += N - 10**3 + 1
    if N >= 10**6:
        ans += N - 10**6 + 1
    if N >= 10**9:
        ans += N - 10**9 + 1
    if N >= 10**12:
        ans += N - 10**12 + 1
    if N >= 10**15:
        ans += N - 10**15 + 1
    # output
    print(ans)
