def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            k = j + (j - i)
            if k >= n:
                continue
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans += 1
    print(r * g * b - ans)
