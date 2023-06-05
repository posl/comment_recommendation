def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    dic = {}
    for i in range(n):
        if s[i] not in dic:
            dic[s[i]] = 1
            print(s[i])
        else:
            dic[s[i]] += 1
            print(s[i] + '(' + str(dic[s[i]]-1) + ')')

if __name__ == '__main__':
    main()