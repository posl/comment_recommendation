def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s2 = []
    for i in range(n):
        if s[i] in s[0:i]:
            s2.append(s[i]+"("+str(s[0:i].count(s[i]))+")")
        else:
            s2.append(s[i])
    for i in range(n):
        print(s2[i])

if __name__ == '__main__':
    main()