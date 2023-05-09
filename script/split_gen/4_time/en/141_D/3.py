def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for a in A:
        ans += a
        if ans % (2 ** M) == 0:
            ans //= 2 ** M
            M -= 1
        else:
            ans //= 2 ** (M - 1)
            M -= 2
    print(ans)
main()
