def main():
    s = input()
    n = len(s)
    ans = 0
    for i in range(n):
        for j in range(i, n):
            t = s[i:j+1]
            if not 'ACGT' in t:
                break
            ans = max(ans, len(t))
    print(ans)
