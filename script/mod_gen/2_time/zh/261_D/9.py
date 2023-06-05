def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if s[i] in s[0:i]:
            j = 1
            while s[i] + '(' + str(j) + ')' in s[0:i]:
                j += 1
            print(s[i] + '(' + str(j) + ')')
        else:
            print(s[i])

if __name__ == '__main__':
    main()