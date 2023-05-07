def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if not 'A' in s[i:j+1] and not 'C' in s[i:j+1] and not 'G' in s[i:j+1] and not 'T' in s[i:j+1]:
                ans = max(ans, j-i+1)
    print(ans)
