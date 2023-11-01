def main():
    n = int(input())
    s = [input() for i in range(n)]
    s = list(set(s))
    s.sort()
    for i in range(len(s)):
        if s[i][0] == '!':
            if s[i][1:] in s:
                print(s[

if __name__ == '__main__':
    main()