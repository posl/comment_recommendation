def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = r * g * b
    for i in range(n):
        for j in range(i + 1, n):
            k = j * 2 - i
            if k < n:
                if s[i] != s[j] and

if __name__ == '__main__':
    main()