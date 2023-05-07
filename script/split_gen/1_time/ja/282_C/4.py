def main():
    n = int(input())
    s = input()
    ans = ""
    count = 0
    for i in range(n):
        if s[i] == '"':
            count += 1
        elif s[i] == ',' and count % 2 == 0:
            ans += '.'
        else:
            ans += s[i]
    print(ans)
