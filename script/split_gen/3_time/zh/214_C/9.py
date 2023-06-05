def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        if i == 0:
            ans[0] = t[0]
        else:
            ans[i] = min(ans[i-1]+s[i-1], t[i])
    for i in range(n):
        print(ans[i])
