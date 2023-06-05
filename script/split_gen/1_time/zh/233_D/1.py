def main():
    print("233_d")
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    s = [0]
    for i in range(n):
        s.append(s[i]+a[i])
    #print(s)
    ans = 0
    r = 0
    for l in range(n):
        while r <= n and s[r] - s[l] < k:
            r += 1
        if s[r] - s[l] == k:
            ans += 1
    print(ans)
