def main():
    s = input()
    n = len(s)
    ans = n
    for i in range(n):
        if s[i] != '0':
            ans += int(s[i]) - 1
    print(ans)
