def main():
    n,k = map(int,input().split())
    r,s,p = map(int,input().split())
    t = input()
    ans = 0
    for i in range(n):
        if t[i] == 'r':
            if i - k >= 0 and t[i-k] == 'r':
                t[i] = 'p'
            else:
                ans += p
        elif t[i] == 's':
            if i - k >= 0 and t[i-k] == 's':
                t[i] = 'r'
            else:
                ans += r
        else:
            if i - k >= 0 and t[i-k] == 'p':
                t[i] = 's'
            else:
                ans += s
    print(ans)
