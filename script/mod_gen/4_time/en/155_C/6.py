def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    max = 0
    for i in range(n):
        if max < s.count(s[i]):
            max = s.count(s[i])
    for i in range(n):
        if max == s.count(s[i]):
            print(s[i])

if __name__ == '__main__':
    main()