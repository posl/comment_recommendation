def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(n):
        if i == 0:
            ans += 1
        else:
            if s[i-1] != s[i]:
                ans += 1
    print(ans)
