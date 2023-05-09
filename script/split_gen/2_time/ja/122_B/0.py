def main():
    s = input()
    ans = 0
    cnt = 0
    for i in range(len(s)):
        if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
            cnt += 1
        else:
            cnt = 0
        ans = max(ans, cnt)
    print(ans)
