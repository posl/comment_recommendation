def main():
    s = input()
    s = s[::-1]
    n = len(s)
    s += '0'
    ans = 0
    for i in range(n):
        if s[i] == '0':
            ans += 1
        else:
            if s[i+1] == '0':
                ans += 1
            else:
                ans += 2
    print(ans)
