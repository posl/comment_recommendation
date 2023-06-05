def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if s[i] in s[:i]:
            j = 1
            while s[i]+ '(' + str(j) + ')' in s[:i]:
                j += 1
            s[i] += '(' + str(j) + ')'
    for i in range(n):
        print(s[i])

if __name__ == '__main__':
    main()