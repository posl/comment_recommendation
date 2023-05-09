def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            k = j + (j - i)
            if k < n and s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
                cnt += 1
    print(r * g * b - cnt)

if __name__ == '__main__':
    main()