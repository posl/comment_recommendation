def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        if i == 0:
            ans[i] = t[i]
        else:
            ans[i] = min(t[i], ans[i - 1] + s[i - 1])
    for a in ans:
        print(a)
