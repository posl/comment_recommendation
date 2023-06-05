def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[i] = t[i]
    for i in range(n):
        if i == 0:
            if t[i] + s[i] < t[n-1]:
                ans[i] = t[i] + s[i]
        else:
            if t[i] + s[i] < t[i-1]:
                ans[i] = t[i] + s[i]
    for i in range(n):
        print(ans[i])
main()
