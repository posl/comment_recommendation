def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        s = str(i)
        ans += s.count(s[0]) * s.count(s[-1])
    print(ans)
