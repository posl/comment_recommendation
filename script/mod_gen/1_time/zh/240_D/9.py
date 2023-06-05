def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * (2 * 10 ** 5 + 1)
    ans = [0] * n
    for i in range(n):
        b[a[i]] += 1
    for i in range(2 * 10 ** 5, 1, -1):
        if b[i] == 0:
            continue
        if b[i] == 1:
            ans[0] += 1
        else:
            ans[0] += 1
            ans[b[i]] -= 1
            ans[b[i] + 1] += 1
    for i in range(1, n):
        ans[i] += ans[i - 1]
    print('\n'.join(map(str, ans)))
main()
