def main():
    s = input()
    s = list(s)
    ans = 0
    tmp = 0
    for i in range(len(s)):
        if s[i] == "A" or s[i] == "C" or s[i] == "G" or s[i] == "T":
            tmp += 1
        else:
            tmp = 0
        ans = max(ans, tmp)
    print(ans)
