def main():
    s = input()
    ans = 0
    cnt = 0
    for i in range(len(s)):
        if s[i] in "ACGT":
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 0
    print(ans)
