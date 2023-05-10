def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if s[i] not in s[:i]:
            print(s[i])
        else:
            print(s[i]+"("+str(s[:i].count(s[i]))+")")

if __name__ == '__main__':
    main()