def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    ans = 0
    for i in range(k):
        if t[i] == 'r':
            ans += p
        elif t[i] == 's':
            ans += r
        else:
            ans += s
    for i in range(k,n):
        if t[i] == t[i-k]:
            t = t[:i] + 'x' + t[i+1:]
        else:
            if t[i] == 'r':
                ans += p
            elif t[i] == 's':
                ans += r
            else:
                ans += s
    print(ans)
