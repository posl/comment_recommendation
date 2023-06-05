def main():
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    candy = {}
    for i in range(k):
        if c[i] not in candy:
            candy[c[i]] = 1
        else:
            candy[c[i]] += 1
    ans = len(candy)
    for i in range(k, n):
        if c[i] not in candy:
            candy[c[i]] = 1
        else:
            candy[c[i]] += 1
        candy[c[i - k]] -= 1
        if candy[c[i - k]] == 0:
            del candy[c[i - k]]
        ans = max(ans, len(candy))
    print(ans)
main()
