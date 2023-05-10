def main():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    ans = [10**9+1]*n
    for i in range(n):
        ans[i] = min(ans[i], t[i])
        ans[(i+1)%n] = min(ans[(i+1)%n], ans[i]+s[i])
    for i in ans:
        print(i)
