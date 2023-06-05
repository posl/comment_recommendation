def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    d = {}
    for i in range(n):
        if s[i] in d:
            d[s[i]] += 1
            print(s[i] + "(" + str(d[s[i]] - 1) + ")")
        else:
            d[s[i]] = 1
            print(s[i])

if __name__ == '__main__':
    main()