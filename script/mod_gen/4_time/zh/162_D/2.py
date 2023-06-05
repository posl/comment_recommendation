def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    total = r * g * b
    for i in range(n):
        for j in range(i + 1, n):
            k = 2 * j - i
            if k >= n:
                continue
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                total -= 1
    print(total)

if __name__ == '__main__':
    main()