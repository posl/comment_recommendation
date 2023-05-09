def main():
    s = input()
    ans = 0
    count = 0
    for i in range(len(s)):
        if s[i] in "ACGT":
            count += 1
        else:
            ans = max(ans, count)
            count = 0
    ans = max(ans, count)
    print(ans)
