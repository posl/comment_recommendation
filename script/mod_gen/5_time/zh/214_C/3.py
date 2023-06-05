def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    for i in range(n):
        t[i] = (t[i], i)
    t.sort()
    ans = [0] * n
    for i in range(n):
        ans[t[i][1]] = t[i][0]
    for i in range(n):
        if ans[i] < s[i]:
            ans[i] = s[i]
        elif ans[i] % s[i] == 0:
            pass
        else:
            ans[i] = s[i] * (ans[i] // s[i] + 1)
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()