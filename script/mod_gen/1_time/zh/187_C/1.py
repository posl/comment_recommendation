def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    for i in range(n-1):
        if s[i][0] == '!' and s[i+1][0] != '!':
            if s[i][1:] == s[i+1]

if __name__ == '__main__':
    main()