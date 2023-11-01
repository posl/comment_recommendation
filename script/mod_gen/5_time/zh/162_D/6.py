def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = r * g * b
    for i in range(n):
        for j in range(1, n):
            k = 2 * j - i
            if k < n and s[i] != s[j]

if __name__ == '__main__':
    main()