def main():
    n = int(input())
    s = input()
    r = s.count('R')
    g = s.count('G')
    b = s.count('B')
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if s[i] != s[j]:

if __name__ == '__main__':
    main()