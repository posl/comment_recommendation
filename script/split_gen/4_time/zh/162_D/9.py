def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = r * g * b
    for i in range(n):
        for j in range(i):
            k = 2 * j - i
            if k < 0:
                continue
            if k >= n:
                continue
            if s[i] == s[j]:
                continue
            if s[j] == s[k]:
                continue
            if s[k] == s[i]:
                continue
            ans -= 1
    print(ans)
