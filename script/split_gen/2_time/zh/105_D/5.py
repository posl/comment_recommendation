def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    s = [0]*(n+1)
    for i in range(n):
        s[i+1] = s[i]+a[i]
    mod = {}
    for i in range(n+1):
        if s[i]%m in mod:
            mod[s[i]%m] += 1
        else:
            mod[s[i]%m] = 1
    ans = 0
    for i in mod:
        ans += mod[i]*(mod[i]-1)//2
    print(ans)
