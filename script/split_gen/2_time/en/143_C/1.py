def main():
    n = int(input())
    s = input()
    ans = 1
    for i in range(n-1):
        if s[i] != s[i+1]:
            ans += 1
    print(ans)
