def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()
    s = [0]*(n+1)
    for i in range(n):
        s[i+1] = s[i] + a[i]
    s.reverse()
    s = s[1:]
    #print(s)
    ans = [0]*n
    for i in range(n):
        ans[i] = s[i]
        for j in range(i+1, n):
            if ans[i] <= a[j]:
                ans[i] = ans[i]
            else:
                ans[i] = ans[i] + a[j]
    ans.reverse()
    for i in range(n):
        print(ans[i])
