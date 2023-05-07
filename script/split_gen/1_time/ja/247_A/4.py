def main():
    s = input()
    ans = ''
    for i in range(len(s)-1):
        ans += s[i+1]
    ans += '0'
    print(ans)
