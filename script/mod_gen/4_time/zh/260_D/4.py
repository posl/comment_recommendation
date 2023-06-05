def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = [0 for _ in range(n)]
    ans[0] = 1
    for i in range(n):
        if i == 0:
            continue
        ans[i] = ans[p[i] - 1] + 1
    for i in range(n):
        if ans[i] > k:
            ans[i] = -1
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()