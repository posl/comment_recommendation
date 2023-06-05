def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    ans = [-1] * n
    ans[0] = k
    for i in range(n):
        if p[i] == 1:
            ans[i] = 1
            break
    for i in range(1, n):
        if ans[i] != -1:
            continue
        x = p[i]
        ans[i] = ans[x - 1]
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()