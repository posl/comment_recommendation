def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s2 = []
    for i in range(n):
        s2.append(s[i])
    for i in range(n):
        if s2.count(s[i]) == 1:
            print(s[i])
        else:
            for j in range(1, s2.count(s[i]) + 1):
                if s[i] not in s2[j:]:
                    print(s[i])
                else:
                    print(s[i] + "(" + str(j) + ")")
                    s2[j] = s[i] + "(" + str(j) + ")"

if __name__ == '__main__':
    main()