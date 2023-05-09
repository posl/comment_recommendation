def main():
    s = input()
    k = int(input())
    n = len(s)
    ans = 0
    if s.count('.') == 0:
        ans = n
    else:
        for i in range(n):
            if s[i] == '.':
                continue
            for j in range(i, n):
                if s[j] == '.':
                    continue
                if j - i + 1 <= k:
                    ans = max(ans, j - i + 1)
                else:
                    break
    print(ans)
