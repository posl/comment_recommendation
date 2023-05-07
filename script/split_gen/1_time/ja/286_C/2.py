def main():
    n, a, b = map(int, input().split())
    s = input()
    ans = 0
    for i in range(n//2):
        if s[i] != s[-(i+1)]:
            ans += b
    if n%2==1:
        if s[n//2] != s[-(n//2+1)]:
            ans += b
    if ans == 0:
        print(0)
    else:
        print(ans+a)
