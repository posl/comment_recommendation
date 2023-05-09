def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if s.count(s[i]) == 1:
            print(s[i])
        else:
            print(s[i]+'('+str(s[:i].count(s[i]))+')')

if __name__ == '__main__':
    main()