def main():
    s = input()
    ans = 0
    tmp = 0
    for i in range(len(s)):
        if s[i] in "ACGT":
            tmp += 1
            ans = max(ans, tmp)
        else:
            tmp = 0
    print(ans)
