def main():
    s = input()
    ans = 0
    tmp = 0
    for i in range(len(s)):
        if s[i] in ['A', 'C', 'G', 'T']:
            tmp += 1
        else:
            tmp = 0
        ans = max(ans, tmp)
    print(ans)
