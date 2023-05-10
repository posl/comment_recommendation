def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    cnt = 0
    for i in range(n):
        for j in range(i+1,n):
            k = 2*j-i
            if k >= n:
                continue
            if s[i] != s[j] and s[j] != s[k] and s[i] != s[k]:
                cnt += 1
    print(r*g*b - cnt)
main()

if __name__ == '__main__':
    main()