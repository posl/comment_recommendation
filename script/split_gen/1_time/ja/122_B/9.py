def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if set(s[i:j]) <= set('ACGT'):
                ans = max(ans, j - i)
    print(ans)
