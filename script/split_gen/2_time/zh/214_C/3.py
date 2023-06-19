def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = [0 for _ in range(n)]
    for i in range(n):
        if i == 0:
            if t[i] <= s[i]:
                ans[i] = t[i]
            else:
                ans[i] = s[i]
        else:
            if t[i] <= s[i] + ans[i-1]:
                ans[i] = t[i]
            else:
                ans[i] = s[i] + ans[i-1]
    for i in range(n):
        print(ans[i])
