def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = r * g * b
    for i in range(n):
        for j in range(i + 1, n):
            if j + (j - i) < n and s[i] != s[j] and s[j] != s[j + (j - i)] and s[i] != s[j + (j - i)]:
                ans -= 1
    print(ans)

if __name__ == '__main__':
    main()