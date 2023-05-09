def main():
    n = int(input())
    s = input()
    r, g, b = s.count("R"), s.count("G"), s.count("B")
    ans = r * g * b
    for i in range(n):
        for j in range(i + 1, n):
            k = 2 * j - i
            if k >= n:
                continue
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans -= 1
    print(ans)
