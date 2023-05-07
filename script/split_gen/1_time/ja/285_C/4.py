def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n-1):
        ans += 26**(i+1)
    ans += ord(s[0]) - ord('A') + 1
    for i in range(1,n):
        ans += (ord(s[i]) - ord('A')) * 26**(n-i)
    print(ans)
