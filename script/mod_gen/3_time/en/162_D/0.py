def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = r * g * b
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                continue
            k = 2 * j - i
            if k >= n:
                continue
            if s[k] == s[i] or s[k] == s[j]:
                continue
            ans -= 1
    print(ans)

if __name__ == '__main__':
    main()